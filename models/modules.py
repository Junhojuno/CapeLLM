"""common modules"""
import math
import torch
import torch.nn as nn


def constant_init(module: nn.Module, val: float, bias: float = 0) -> None:
    if hasattr(module, 'weight') and module.weight is not None:
        nn.init.constant_(module.weight, val)
    if hasattr(module, 'bias') and module.bias is not None:
        nn.init.constant_(module.bias, bias)


def normal_init(module: nn.Module,
                mean: float = 0,
                std: float = 1,
                bias: float = 0) -> None:
    if hasattr(module, 'weight') and module.weight is not None:
        nn.init.normal_(module.weight, mean, std)
    if hasattr(module, 'bias') and module.bias is not None:
        nn.init.constant_(module.bias, bias)


def inverse_sigmoid(x, eps=1e-3):
    x = x.clamp(min=0, max=1)
    x1 = x.clamp(min=eps)
    x2 = (1 - x).clamp(min=eps)
    return torch.log(x1 / x2)


class LayerScale(nn.Module):
    """LayerScale layer.
    https://github.com/open-mmlab/mmcv/blob/5916fbd8789f9578cff4d325b1ffe0bc710b4534/mmcv/cnn/bricks/scale.py#L24

    Args:
        dim (int): Dimension of input features.
        inplace (bool): Whether performs operation in-place.
            Default: `False`.
        data_format (str): The input data format, could be 'channels_last'
            or 'channels_first', representing (B, C, H, W) and
            (B, N, C) format data respectively. Default: 'channels_last'.
        scale (float): Initial value of scale factor. Default: 1.0
    """

    def __init__(self,
                 dim: int,
                 inplace: bool = False,
                 data_format: str = 'channels_last',
                 scale: float = 1e-5):
        super().__init__()
        assert data_format in ('channels_last', 'channels_first'), \
            "'data_format' could only be channels_last or channels_first."
        self.inplace = inplace
        self.data_format = data_format
        self.weight = nn.Parameter(torch.ones(dim) * scale)

    def forward(self, x) -> torch.Tensor:
        if self.data_format == 'channels_first':
            shape = tuple((1, -1, *(1 for _ in range(x.dim() - 2))))
        else:
            shape = tuple((*(1 for _ in range(x.dim() - 1)), -1))
        if self.inplace:
            return x.mul_(self.weight.view(*shape))
        else:
            return x * self.weight.view(*shape)


class FFN(nn.Module):

    def __init__(self,
                 embed_dims=256,
                 feedforward_channels=2048,
                 num_fcs=2,
                 ffn_drop=0.,
                 dropout=0.,
                 add_identity=True,
                 layer_scale_init_value=0.):
        super().__init__()
        self.embed_dims = embed_dims
        self.feedforward_channels = feedforward_channels
        self.num_fcs = num_fcs

        layers = []
        in_channels = embed_dims
        for _ in range(num_fcs - 1):
            layers.append(
                nn.Sequential(
                    nn.Linear(in_channels, feedforward_channels),
                    nn.ReLU(inplace=True),
                    nn.Dropout(ffn_drop)))
            in_channels = feedforward_channels
        layers.append(nn.Linear(feedforward_channels, embed_dims))
        layers.append(nn.Dropout(ffn_drop))
        self.layers = nn.Sequential(*layers)
        self.dropout_layer = \
            nn.Dropout(dropout) \
            if dropout != 0. \
            else torch.nn.Identity()
        self.add_identity = add_identity

        if layer_scale_init_value > 0:
            self.gamma2 = LayerScale(embed_dims, scale=layer_scale_init_value)
        else:
            self.gamma2 = nn.Identity()

    def forward(self, x, identity=None):
        """Forward function for `FFN`.

        The function would add x to the output tensor if residue is None.
        """
        out = self.layers(x)
        out = self.gamma2(out)
        if not self.add_identity:
            return self.dropout_layer(out)
        if identity is None:
            identity = x
        return identity + self.dropout_layer(out)


class MultiHeadAttention(nn.Module):

    def __init__(self,
                 embed_dims,
                 num_heads,
                 attn_drop=0.,
                 proj_drop=0.,
                 dropout: float = 0.,
                 **kwargs):
        super().__init__()
        self.embed_dims = embed_dims
        self.num_heads = num_heads

        self.attn = nn.MultiheadAttention(embed_dims, num_heads, attn_drop,
                                          **kwargs)

        self.proj_drop = nn.Dropout(proj_drop)
        self.dropout_layer = nn.Dropout(dropout)

    def forward(self,
                query,
                key=None,
                value=None,
                identity=None,
                query_pos=None,
                key_pos=None,
                attn_mask=None,
                key_padding_mask=None,
                need_weights: bool = False,
                **kwargs):
        if key is None:
            key = query
        if value is None:
            value = key
        if identity is None:
            identity = query

        if (key_pos is None) and (query_pos is not None):
            if query_pos.shape == key.shape:
                key_pos = query_pos
            else:
                import warnings
                warnings.warn(f'position encoding of key is'
                              f'missing in {self.__class__.__name__}.')

        if query_pos is not None:
            query = query + query_pos
        if key_pos is not None:
            key = key + key_pos

        # NOTE - inputs are always batch first!
        query = query.transpose(0, 1)
        key = key.transpose(0, 1)
        value = value.transpose(0, 1)

        out, attn_weights = self.attn(
            query=query,
            key=key,
            value=value,
            attn_mask=attn_mask,
            key_padding_mask=key_padding_mask,
            need_weights=need_weights
        )
        out = out.transpose(0, 1)
        out = identity + self.dropout_layer(self.proj_drop(out))
        if attn_weights is not None:
            return out, attn_weights
        return out


class SinusoidalPositionEncoding(nn.Module):
    """Position encoding with sine and cosine functions.

    See `End-to-End Object Detection with Transformers
    <https://arxiv.org/pdf/2005.12872>`_ for details.

    Args:
        num_feats (int): The feature dimension for each position
            along x-axis or y-axis. Note the final returned dimension
            for each position is 2 times of this value.
        temperature (int, optional): The temperature used for scaling
            the position embedding. Default 10000.
        normalize (bool, optional): Whether to normalize the position
            embedding. Default False.
        scale (float, optional): A scale factor that scales the position
            embedding. The scale will be used only when `normalize` is True.
            Default 2*pi.
        eps (float, optional): A value added to the denominator for
            numerical stability. Default 1e-6.
    """

    def __init__(self,
                 num_feats,
                 temperature=10000,
                 normalize=False,
                 scale=2 * math.pi,
                 eps=1e-6):
        super().__init__()
        if normalize:
            assert isinstance(scale, (float, int)), 'when normalize is set,' \
                'scale should be provided and in float or int type, ' \
                f'found {type(scale)}'
        self.num_feats = num_feats
        self.temperature = temperature
        self.normalize = normalize
        self.scale = scale
        self.eps = eps

    def forward(self, mask):
        """Forward function for `SinePositionalEncoding`.

        Args:
            mask (Tensor): ByteTensor mask. Non-zero values representing
                ignored positions, while zero values means valid positions
                for this image. Shape [bs, h, w].

        Returns:
            pos (Tensor): Returned position embedding with shape
                [bs, num_feats*2, h, w].
        """
        not_mask = ~mask
        y_embed = not_mask.cumsum(1, dtype=torch.float32)
        x_embed = not_mask.cumsum(2, dtype=torch.float32)
        if self.normalize:
            y_embed = y_embed / (y_embed[:, -1:, :] + self.eps) * self.scale
            x_embed = x_embed / (x_embed[:, :, -1:] + self.eps) * self.scale
        dim_t = torch.arange(
            self.num_feats, dtype=torch.float32, device=mask.device)
        dim_t = self.temperature**(2 * (dim_t // 2) / self.num_feats)
        pos_x = x_embed[:, :, :, None] / dim_t
        pos_y = y_embed[:, :, :, None] / dim_t
        pos_x = torch.stack(
            (pos_x[:, :, :, 0::2].sin(), pos_x[:, :, :, 1::2].cos()),
            dim=4).flatten(3)
        pos_y = torch.stack(
            (pos_y[:, :, :, 0::2].sin(), pos_y[:, :, :, 1::2].cos()),
            dim=4).flatten(3)
        pos = torch.cat((pos_y, pos_x), dim=3).permute(0, 3, 1, 2)
        return pos

    def forward_coordinates(self, coord):
        """
        https://github.com/flyinglynx/CapeFormer/blob/4ead46b9c3a3a924d7b674adf8fd71ec4b430eed/capeformer/models/utils/positional_encoding.py#L96C5-L122C19
        Forward funtion for normalized coordinates input with the shape of [bs, kpt, 2]
        return:
            pos (Tensor): position embedding with the shape of [bs, kpt, num_feats*2]
        """
        x_embed, y_embed = coord[:, :, 0], coord[:, :, 1]  # [bs, kpt]
        x_embed = x_embed * self.scale  # [bs, kpt]
        y_embed = y_embed * self.scale

        dim_t = torch.arange(
            self.num_feats, dtype=torch.float32, device=coord.device)
        dim_t = self.temperature**(2 * (dim_t // 2) / self.num_feats)

        pos_x = x_embed[:, :, None] / dim_t   # [bs, kpt, num_feats]
        pos_y = y_embed[:, :, None] / dim_t   # [bs, kpt, num_feats]
        bs, kpt, _ = pos_x.shape

        pos_x = torch.stack(
            (pos_x[:, :, 0::2].sin(), pos_x[:, :, 1::2].cos()),
            dim=3).view(bs, kpt, -1)  # [bs, kpt, num_feats]
        pos_y = torch.stack(
            (pos_y[:, :, 0::2].sin(), pos_y[:, :, 1::2].cos()),
            dim=3).view(bs, kpt, -1)  # [bs, kpt, num_feats]
        pos = torch.cat((pos_y, pos_x), dim=2)  # [bs, kpt, num_feats * 2]

        return pos

    def __repr__(self):
        """str: a string that describes the module"""
        repr_str = self.__class__.__name__
        repr_str += f'(num_feats={self.num_feats}, '
        repr_str += f'temperature={self.temperature}, '
        repr_str += f'normalize={self.normalize}, '
        repr_str += f'scale={self.scale}, '
        repr_str += f'eps={self.eps})'
        return repr_str
