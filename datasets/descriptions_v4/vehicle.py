# CarFusion(13)
# NOTE - 3개의 category가 모두 동일한 keypoint definition을 따른다.
# capex에서 발췌(https://github.com/matanr/capex/blob/main/models/datasets/datasets/mp100/utils.py)
# REVIEW - left가 실제 left!
# FIXME - windshield -> exhaust로 수정 완료(CapeX 오류)
# NOTE - 용어 통일화 작업 완료!
vehicle = {
    "right front wheel": "The right front wheel is a point at the center of right front wheel, located on the right-hand side of the vehicle. it is situated in front of the right rear wheel.",
    "left front wheel": "The left front wheel is a point at the center of left front wheel, positioned on the left-hand side of the vehicle. it is situated in front of the left rear wheel.",
    "right rear wheel": "The right rear wheel is a point at the center of right rear wheel, positioned on the right-hand side of the vehicle. it is situated behind the right front wheel.",
    "left rear wheel": "The left rear wheel is a point at the center of left rear wheel, positioned on the left-hand side of the vehicle. it is situated behind the left front wheel.",
    "right headlight": "The right headlight is a point at the center of right headlight, located on the right-hand side of the vehicle. it is located above the right front wheel and to the right of the left headlight.",
    "left headlight": "The left headlight is a point at the center of left headlight, located on the left-hand side of the vehicle. it is located above the left front wheel and to the left of the right headlight.",
    "right taillight": "The right taillight is a point at the center of right tailight which is the right rear light located on the right-hand side of the vehicle. it is located above the right rear wheel and to the right of the left taillight.",
    "left taillight": "The left taillight is a point at the center of left tailight which is the left rear light located on the left-hand side of the vehicle. it is located above the left rear wheel and to the left of the right taillight.",
    "exhaust": "The exhaust is a point that represents the vehicle exhaust port, positioned near the rear wheels and under the taillights.",
    "right front of roof": "The right front of roof is a point at the right front corner of vehicle roof, positioned on the front side of vehicle and situnated to the right of the left front of roof and in front of the right rear of roof.",
    "left front of roof": "The left front of roof is a point at the left front corner of vehicle roof, positioned on the front side of vehicle and situnated to the left of the right front of roof and in front of the left rear of roof.",
    "right rear of roof": "The right rear of roof is a point at the right front corner of vehicle roof, positioned on the rear side of vehicle and situnated to the right of the left rear of roof and behind the right front of roof.",
    "left rear of roof": "The left rear of roof is a point at the left front corner of vehicle roof, positioned on the rear side of vehicle and situnated to the left of the right rear of roof and behind the left front of roof.",
}
