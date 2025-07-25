import numpy as np


def _calc_distances(preds, targets, mask, normalize):
    N, K, _ = preds.shape
    # set mask=0 when normalize==0
    _mask = mask.copy()
    _mask[np.where((normalize == 0).sum(1))[0], :] = False
    distances = np.full((N, K), -1, dtype=np.float32)
    # handle invalid values
    normalize[np.where(normalize <= 0)] = 1e6
    distances[_mask] = np.linalg.norm(
        ((preds - targets) / normalize[:, None, :])[_mask], axis=-1)
    return distances.T


def _distance_acc(distances, thr=0.5):
    distance_valid = distances != -1
    num_distance_valid = distance_valid.sum()
    if num_distance_valid > 0:
        return (distances[distance_valid] < thr).sum() / num_distance_valid
    return -1


def keypoint_pck_accuracy(pred: np.ndarray,
                          gt: np.ndarray,
                          mask: np.ndarray,
                          thr: float,
                          normalize: np.ndarray) -> tuple[np.ndarray, float, int]:
    """PCK@thr 계산

    Args:
        pred (np.ndarray): model prediction; (B, K, 2)
        gt (np.ndarray): ground truth; (B, K, 2)
        mask (np.ndarray): keypoint visibilities(boolean); (B, K)
        thr (float): distance threshold
        normalize (np.ndarray): normalizer to 0~1; (B, 2)

    Returns:
        tuple[np.ndarray, float, int]:
            - acc:      acc per example,
            - avg_acc:  avg acc of batch examples,
            - cnt:      # valid examples
    """
    distances = _calc_distances(pred, gt, mask, normalize)

    acc = np.array([_distance_acc(d, thr) for d in distances])
    valid_acc = acc[acc >= 0]
    cnt = len(valid_acc)
    avg_acc = valid_acc.mean() if cnt > 0 else 0
    return acc, avg_acc, cnt
