# COCO(17)
# https://github.com/kennethwdk/LocLLM/blob/b33cb2f43ea7ed43606afb27dd04b0e44ceacae5/datasets/constants.py#L12
# REVIEW - left가 실제 left!
human_body = {
    'nose': 'The nose is the central point of face, protruding feature on the face, located just above the upper lip.',
    'left eye': 'The left eye is the visual organ on the left side of their face, typically located above the left cheek and beside the nose.',
    'right eye': 'The right eye is the visual organ on the right side of their face, typically located above the right cheek and beside the nose.',
    'left ear': 'The left ear is the auditory organ on the left side of their head, typically located to the side of the left temple.',
    'right ear': 'The right ear is the auditory organ on the right side of their head, typically located to the side of the right temple.',
    'left shoulder': 'The left shoulder is the joint connecting the left arm and the torso, typically situated on the upper left side of the chest.',
    'right shoulder': 'The right shoulder is the joint connecting the right arm and the torso, typically situated on the upper right side of the chest.',
    'left elbow': 'The left elbow is the joint connecting the left upper arm and the left forearm, typically situated in the middle of the left arm, between left shoulder and left wrist.',
    'right elbow': 'The right elbow is the joint connecting the right upper arm and the right forearm, typically situated in the middle of the right arm, between right shoulder and right wrist.',
    'left wrist': 'The left wrist is the joint connecting the left forearm and the left hand, typically located at the base of the left hand.',
    'right wrist': 'The right wrist is the joint connecting the right forearm and the right hand, typically located at the base of the right hand.',
    'left hip': 'The left hip is the joint connecting the left thigh to the pelvis, typically located on the left side of the lower torso.',
    'right hip': 'The right hip is the joint connecting the right thigh to the pelvis, typically located on the right side of the lower torso.',
    'left knee': 'The left knee is the joint connecting the left thigh and the left lower leg, typically situated in the middle of the left leg, it is located between the left hip and left ankle.',
    'right knee': 'The right knee is the joint connecting the upper leg and lower leg on the right side, it is located between the right hip and right ankle.',
    'left ankle': 'The left ankle is the joint connecting the left lower leg and the left foot, typically located at the base of the left leg.',
    'right ankle': 'The right ankle is the joint connecting the right lower leg and the right foot, typically located at the base of the right leg.',
}

# 300W(68) id=40
# keypoint type이 annotation file에 정의되어있지 않음
# NOTE - capex에서 발췌(https://github.com/matanr/capex/blob/main/models/datasets/datasets/mp100/utils.py)
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 1st -> first, 2nd -> second, ...
human_face = {
    "right chin first": "The right chin first is the rightmost point of the chin, marking the start of the jawline on the right side of the face. it is usually on the right sideburn.",
    "right chin second": "The right chin second is the second point on the right side of the chin, positioned under the rightmost point of the chin. it is usually on the end of right sideburn and the center of right ear.",
    "right chin third": "The right chin third is the third point on the right side of the chin, positioned closer to the right earlobe and under the right chin second.",
    "right jawline first": "The right jawline first is the starting point of right jawline forward to the center chin and on the right side of the chin, positioned under the right chin third.",
    "right jawline second": "The right jawline second is on the right jawline forward to the center chin and on the right side of the chin, positioned under the right jawline first.",
    "right jawline third": "The right jawline third is on the right jawline forward to the center chin and on the right side of the chin, positioned under the right jawline second.",
    "right jawline fourth": "The right jawline fourth is the end point of the right jawline forward to the center chin and on the right bottom side of the chin, positioned under the right jawline third.",
    "center chin right": "the center chin right is on the bottom of chin, located on the right of center chin. it is positioned under the area of right side of the bottom lip center. it is on the right of the center chin.",
    "center chin": "The center chin is the central point of the chin, marking the bottom-most point of the face. it is positioned directly under the lip bottom center and between the center chin left and the center chin right.",
    "center chin left": "the center chin left is on the bottom of chin, located on the left of center chin. it is positioned under the area of left side of the bottom lip center. it is on the left of the center chin.",
    "left jawline fourth": "The left jawline fourth is the end point of the left jawline forward to the center chin and on the left bottom side of the chin, positioned under the left jawline third.",
    "left jawline third": "The left jawline third is on the left jawline forward to the center chin and on the left side of the chin, positioned under the left jawline second.",
    "left jawline second": "The left jawline second is on the left jawline forward to the center chin and on the left side of the chin, positioned under the left jawline first.",
    "left jawline first": "The left jawline first is the starting point of left jawline forward to the center chin and on the left side of the chin, positioned under the left chin third.",
    "left chin third": "The left chin third is the third point on the left side of the chin, positioned closer to the left earlobe and under the left chin second.",
    "left chin second": "The left chin second is the second point on the left side of the chin, positioned under the leftmost point of the chin. it is usually on the end of left sideburn and the center of left ear.",
    "left chin first": "The left chin first is the leftmost point of the chin, marking the start of the jawline on the left side of the face. it is usually on the left sideburn.",
    "right eyebrow outer": "The right eyebrow outer is the outer edge of the right eyebrow, closest to the right temple.",
    "right eyebrow outer middle": "The right eyebrow outer middle is a point on the right eyebrow, positioned between the outer edge and the center.",
    "right eyebrow middle": "The right eyebrow middle is the central point of the right eyebrow. it is located above the right eye's upper area, specifically the right eye outer top and the right eye inner top.",
    "right eyebrow inner middle": "The right eyebrow inner middle is a point on the right eyebrow, positioned between the right eyebrow middle and the right eyebrow inner.",
    "right eyebrow inner": "The right eyebrow inner is the inner edge of the right eyebrow, closest to the bridge of the nose. it is positioned on the left of the right eyebrow inner middle. the forehead is located on the left to this point.",
    "left eyebrow inner": "The left eyebrow inner is the inner edge of the left eyebrow, closest to the bridge of the nose. it is positioned on the right of the left eyebrow inner middle. the forehead is located on the right to this point.",
    "left eyebrow inner middle": "The left eyebrow inner middle is a point on the left eyebrow, positioned between the center and the inner edge.",
    "left eyebrow middle": "The left eyebrow middle is the central point of the left eyebrow. it is located above the left eye's upper area, specifically the left eye outer top and the left eye inner top.",
    "left eyebrow outer middle": "The left eyebrow outer middle is a point on the left eyebrow, positioned between the outer edge and the center.",
    "left eyebrow outer": "The left eyebrow outer is the outermost point of the left eyebrow, closest to the left temple.",
    "nose bridge top": "The nose bridge top is the topmost point of the nose bridge, positioned between the eyebrows.",
    "nose bridge middle": "The nose bridge middle is the middle point of the nose bridge, positioned under the top of nose bridge.",
    "nose bridge bottom": "The nose bridge bottom is the bottom point of the nose bridge and at the left above the nose tip.",
    "nose tip": "The nose tip is the tip of the nose, marking the most protruding point of the nose. it is positioned at the bottom of the nose between the nostrils.",
    "right nostril outer": "The right nostril outer is the outer edge of the right nostril. it is positioned on the right of the right nostril inner.",
    "right nostril inner": "The right nostril inner is the inner edge of the right nostril. it is positioned on the left of the right nostril outer. it is also between the nostril center and the right nostril outer.",
    "nostril center": "The nostril center is the center point of the nostril, place left over the philtrum.",
    "left nostril inner": "The left nostril inner is the inner edge of the left nostril. it is positioned on the right of the left nostril outer. it is also between the nostril center and the left nostril outer.",
    "left nostril outer": "The left nostril outer is the outer edge of the left nostril. it is positioned on the left of the left nostril inner.",
    "right eye outer": "The right eye outer is the outer corner of the right eye. it is located opposite the right eye inner, on the right side of the right eye outer top and right eye outer bottom.",
    "right eye outer top": "The right eye outer top is the top edge of the right eye, on the left side of the right eye outer.",
    "right eye inner top": "The right eye inner top is the top edge of the right eye, on the right side of the right eye inner.",
    "right eye inner": "The right eye inner is the inner corner of the right eye, positioned on the right side of the nose bridge.",
    "right eye inner bottom": "The right eye inner bottom is the bottom edge of the right eye, near the inner corner.",
    "right eye outer bottom": "The right eye outer bottom is the bottom edge of the right eye, near the outer corner.",
    "left eye inner": "The left eye inner is the inner corner of the left eye, positioned on the left side of the nose bridge.",
    "left eye inner top": "The left eye inner top is the top edge of the left eye, near the inner corner.",
    "left eye outer top": "The left eye outer top is the top edge of the left eye, near the outer corner.",
    "left eye outer": "The left eye outer is the outer corner of the left eye. it is located opposite the left eye inner, on the left side of the left eye outer top and left eye outer bottom.",
    "left eye outer bottom": "The left eye outer bottom is the bottom edge of the left eye, near the outer corner.",
    "left eye inner bottom": "The left eye inner bottom is the bottom edge of the left eye, near the inner corner.",
    "right lip outer": "The right lip outer is the right corner of the mouth.  it is on the right edge of the mouth and right side of the right lip outer top, the right lip inner, and the right lip bottom.",
    "right lip outer top": "The right lip outer top is a point on the top edge of the upper lip, near the right corner.",
    "right lip top": "The right lip top is the highest point of the right side of the upper lip.",
    "lip top center": "The lip top center is the center point of the upper lip, also known as the Cupid's bow.",
    "left lip top": "The left lip top is the highest point of the left side of the upper lip.",
    "left lip outer top": "The left lip outer top is a point on the top edge of the upper lip, near the left corner.",
    "left lip outer": "The left lip outer is the left corner of the mouth. it is on the left edge of the mouth and left side of the left lip outer top, the left lip inner, and the left lip bottom.",
    "left lip outer bottom": "The left lip outer bottom is a point on the bottom edge of the lower lip, near the left corner.",
    "left lip bottom": "The left lip bottom is the lowest point of the left side of the lower lip.",
    "lip bottom center": "The lip bottom center is the center point of the lower lip. it is the lowest point of the mouth, positioned between the left lip bottom and the right lip bottom.",
    "right lip bottom": "The right lip bottom is the lowest point of the right side of the lower lip.",
    "right lip outer bottom": "The right lip outer bottom is a point on the bottom edge of the lower lip, near the right corner.",
    "right lip inner": "The right lip inner is the inner edge of the lip on the right side. this point is on the left of the right lip outer and under the right lip outer top.",
    "right lip inner top": "The right lip inner top is a point on the top edge of the upper lip, near the right corner. it is under the right lip top.",
    "lip inner top center": "The lip inner top center is the center point of the inner edge of the upper lip.",
    "left lip inner top": "The left lip inner top is a point on the top edge of the upper lip, near the left corner. it is under the left lip top.",
    "left lip inner": "The left lip inner is the inner edge of the lip on the left side. this point is on the right of the left lip outer and under the left lip outer top.",
    "left lip inner bottom": "The left lip inner bottom is the inner edge of the lower lip on the left side.",
    "lip inner bottom center": "The lip inner bottom center is the center point of the inner edge of the lower lip.",
    "right lip inner bottom": "The right lip inner bottom is the inner edge of the lower lip on the right side.",
}


# AFLW(original 21 keypoints -> use 19 keypoints in CAPE)
# human face(id=18)인데 다른 데이터에서 가져온 거라 amur_tiger_body로 되어있음
# 귓볼 2개가 빠짐
# keypoint type이 annotation file에 정의되어있지 않음
# NOTE - capex에서 발췌(https://github.com/matanr/capex/blob/main/models/datasets/datasets/mp100/utils.py)
# ANCHOR - 검수 완료!!
amur_tiger_body = {
    "left side of the left eyebrow": "The left side of the left eyebrow is the outermost point on the left eyebrow, located near the left temple and above the outer corner of the left eye.",
    "middle side of the left eyebrow": "The middle side of the left eyebrow is the midpoint on the left eyebrow, situated between the inner and outer edges of the eyebrow, above the center of the left eye.",
    "right side of the left eyebrow": "The right side of the left eyebrow is the innermost point on the left eyebrow, positioned near the middle of the forehead and above the inner corner of the left eye.",
    "left side of the right eyebrow": "The left side of the right eyebrow is the innermost point on the right eyebrow, positioned near the middle of the forehead and above the inner corner of the right eye.",
    "middle side of the right eyebrow": "The middle side of the right eyebrow is the midpoint on the right eyebrow, situated between the inner and outer edges of the eyebrow, above the center of the right eye.",
    "right side of the right eyebrow": "The right side of the right eyebrow is the outermost point on the right eyebrow, located near the right temple and above the outer corner of the right eye.",
    "left side of the left eye": "The left side of the left eye is the outer corner of the left eye, where the upper and lower eyelids meet.",
    "middle side of the left eye": "The middle side of the left eye is the midpoint on the left eye, positioned along the center of the eye.",
    "right side of the left eye": "The right side of the left eye is the inner corner of the left eye, where the upper and lower eyelids meet.",
    "left side of the right eye": "The left side of the right eye is the inner corner of the right eye, where the upper and lower eyelids meet.",
    "middle side of the right eye": "The middle side of the right eye is the midpoint on the right eye, positioned along the center of the eye.",
    "right side of the right eye": "The right side of the right eye is the outer corner of the right eye, where the upper and lower eyelids meet.",
    "left side of the nose": "The left side of the nose is the left side point of the nose, marking the edge of the left nostril.",
    "middle of the nostrils": "The middle of the nostrils is the central point between the nostrils, positioned at the bottom tip of the nose.",
    "right side of the nose": "The right side of the nose is the right side point of the nose, marking the edge of the right nostril.",
    "left side of the lips": "The left side of the lips is the leftmost point on the lips, at the left corner of the mouth.",
    "mouth": "The mouth is the central point of the mouth, positioned at the center of of the point where the upper and lower lips meet.",
    "right side of the lips": "The right side of the lips is the rightmost point on the lips, at the right corner of the mouth.",
    "chin": "The chin is the central point of the chin, located directly below the lower lip."
}

# OneHand10K(21)
# keypoint type이 정의되어있으나, 직관적으로 구분하기위해
# NOTE - capex에서 발췌(https://github.com/matanr/capex/blob/main/models/datasets/datasets/mp100/utils.py)
# ANCHOR - 검수 완료!!
human_hand = {
    "base of the hand": "The base of the hand is the central point at the base of the hand, where the wrist meets the palm.",
    "base of the thumb": "The base of the thumb is the point at the base of the thumb, where it connects to the palm, near the base of the hand.",
    "first thumb joint": "The first thumb joint is the first joint on the thumb, located between the base of the Thumb and the second thumb joint.",
    "second thumb joint": "The second thumb joint is the second joint on the thumb, located between the first thumb joint and the tip of the thumb.",
    "tip of the thumb": "The tip of the thumb is the tip of the thumb, the uppermost point on the thumb, above the second thumb joint.",
    "base of the index finger": "The base of the index finger is the point at the base of the index finger, where it connects to the palm, near the base of middle finger.",
    "first index finger joint": "The first index finger joint is the first joint on the index finger, located between the base of the index finger and the second index finger joint.",
    "second index finger joint": "The second index finger joint is the second joint on the index finger, located between the first index finger joint and the tip of the index finger.",
    "tip of the index finger": "The tip of the index finger is the tip of the index finger, the uppermost point on the index finger, above the second index finger joint.",
    "base of the middle finger": "The base of the middle finger is the point at the base of the middle finger, where it connects to the palm, between the base of the index finger and the base of the ring finger.",
    "first middle finger joint": "The first middle finger joint is the first joint on the middle finger, located between the base of the middle finger and the second middle finger Joint.",
    "second middle finger joint": "The second middle finger joint is the second joint on the middle finger, located between the first middle finger joint and the tip of the middle joint.",
    "tip of the middle finger": "The tip of the middle finger is the tip of the middle finger, the uppermost point on the middle finger, above the second middle finger joint.",
    "base of the ring finger": "The base of the ring finger is the point at the base of the ring finger, where it connects to the palm, between the two bases, middle finger and little(baby finger).",
    "first ring finger joint": "The first ring finger joint is the first joint on the ring finger, located between the base of the ring finger and the second ring finger joint.",
    "second ring finger joint": "The second ring finger joint is the second joint on the ring finger, located between the first ring finger joint and the tip of the ring finger.",
    "tip of the ring finger": "The tip of the ring finger is the tip of the ring finger, the uppermost point on the ring finger, above the second ring finger joint.",
    "base of the little finger": "The base of the little finger is the point at the base of the little finger, where it connects to the palm, next to the base of the ring finger.",
    "first little finger joint": "The first little finger joint is the first joint on the little finger, located between the base of the little finger and the second little finger joint.",
    "second little finger joint": "The second little finger joint is the second joint on the little finger, located between the first little finger joint and the tip of the little finger.",
    "tip of the little finger": "The tip of the little finger is the tip of the little finger, the uppermost point on the little finger, above the second little finger joint."
}
