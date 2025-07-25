"""용어 통일하는 작업 진행"""
# DeepFashion2
# keypoint type이 정의되어있으나, 직관적으로 구분하기위해
# 모두 capex에서 발췌(https://github.com/matanr/capex/blob/main/models/datasets/datasets/mp100/utils.py)
# long_sleeved_dress = 37 keypoints
# NOTE - keypoint type에 중복이 있음
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
long_sleeved_dress = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder seam.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "center front neckline": "The center front neckline is the center point on the front side of neckline. it connects the right front necklines and left front necklines, located between the right and left front necklines. ",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder seam.",
    "right shoulder seam": "The right shoulder seam is a point on the right shoulder, located on the edge of right shoulder. it connects the right back neckline and the outer top of right sleeve.",
    "outer top of right sleeve": "The outer top of right sleeve is a point on the outer side of the right sleeve, positioned on the top of right sleeve. it connects the right shoulder seam and the right sleeve, between the right shoulder seam and the outer upper point of right sleeve.",
    "outer upper point of right sleeve": "The outer upper point of right sleeve is the point on the outer side of the right sleeve, positioned between the outer top of right sleeve and the outer lower point of right sleeve.",
    "outer lower point of right sleeve": "The outer lower point of right sleeve is the point on the outer side of the right sleeve, positioned between the outer upper point of right sleeve and the outer bottom of right sleeve.",
    "outer bottom of right sleeve": "The outer bottom of right sleeve is the bottom point on the outer side of the right sleeve, positioned under the outer lower point of right sleeve. it is connected to outer lower point of right sleeve and the inner bottom of right sleeve.",
    "inner bottom of right sleeve": "The inner bottom of right sleeve is the bottom point on the inner side of the right sleeve, positioned under the inner lower point of right sleeve. it is connected to inner lower point of right sleeve and the outer bottom of right sleeve.",
    "inner lower point of right sleeve": "The inner lower point of right sleeve is the point on the inner side of the right sleeve, positioned between the inner upper point of right sleeve and the inner bottom of right sleeve.",
    "inner upper point of right sleeve": "The inner upper point of right sleeve is the point on the inner side of the right sleeve, positioned between the inner top of right sleeve and the inner lower point of right sleeve.",
    "inner top of right sleeve": "The inner top of right sleeve is a point on the inner side of the right sleeve, positioned on the top of right sleeve. it connects the right armpit and the right sleeve, between the right armpit and the inner upper point of right sleeve.",
    "right armpit": "The right armpit is a point connecting the right sleeve and the right side of body, located above top of right side seam.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the right armpit and the upper point of right side seam, and connects them.",
    "upper point of right side seam": "The upper point of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the middle of right side seam, and connects them.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the upper point of right side seam and the lower point of right side seam, and connects them.",
    "lower point of right side seam": "The lower point of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the middle of right side seam and the bottom of right side seam, and connects them.",
    "bottom of right side seam": "The bottom of right side seam is bottom edge on the right side seam which means the line of right side of body. it is positioned under the lower point of right side seam and right to the center hem.",
    "center hem": "The center hem is the centeral point on the hem which means bottom edge of a piece of cloth, positioned between the bottom of right side seam and the bottom of left side seam.",
    "bottom of left side seam": "The bottom of left side seam is bottom edge on the left side seam which means the line of left side of body. it is positioned under the lower point of left side seam and left to the center hem.",
    "lower point of left side seam": "The lower point of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the middle of left side seam and the bottom of left side seam, and connects them.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the upper point of left side seam and the lower point of left side seam, and connects them.",
    "upper point of left side seam": "The upper point of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the middle of left side seam, and connects them.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the left armpit and the upper point of left side seam, and connects them.",
    "left armpit": "The left armpit is a point connecting the left sleeve and the left side of body, located above top of left side seam.",
    "inner top of left sleeve": "The inner top of left sleeve is a point on the inner side of the left sleeve, positioned on the top of left sleeve. it connects the left armpit and the left sleeve, between the left armpit and the inner upper point of left sleeve.",
    "inner upper point of left sleeve": "The inner upper point of left sleeve is the point on the inner side of the left sleeve, positioned between the inner top of left sleeve and the inner lower point of left sleeve.",
    "inner lower point of left sleeve": "The inner lower point of left sleeve is the point on the inner side of the left sleeve, positioned between the inner upper point of left sleeve and the inner bottom of left sleeve.",
    "inner bottom of left sleeve": "The inner bottom of left sleeve is the bottom point on the inner side of the left sleeve, positioned under the inner lower point of left sleeve. it is connected to inner lower point of left sleeve and the outer bottom of left sleeve.",
    "outer bottom of left sleeve": "The outer bottom of left sleeve is the bottom point on the outer side of the left sleeve, positioned under the outer lower point of left sleeve. it is connected to outer lower point of left sleeve and the inner bottom of left sleeve.",
    "outer lower point of left sleeve": "The outer lower point of left sleeve is the point on the outer side of the left sleeve, positioned between the outer upper point of left sleeve and the outer bottom of left sleeve.",
    "outer upper point of left sleeve": "The outer upper point of left sleeve is the point on the outer side of the left sleeve, positioned between the outer top of left sleeve and the outer lower point of left sleeve.",
    "outer top of left sleeve": "The outer top of left sleeve is a point on the outer side of the left sleeve, positioned on the top of left sleeve. it connects the left shoulder seam and the left sleeve, between the left shoulder seam and the outer upper point of left sleeve.",
    "left shoulder seam": "The left shoulder seam is a point on the left shoulder, located on the edge of left shoulder. it connects the left back neckline and the outer top of left sleeve.",
}


# 39 keypoints
# ANCHOR - 직접 설명 수정 및 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
long_sleeved_outwear = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder seam.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "top of right placket": "The top of right placket is a point on the right placket, positioned on the top edge of right placket and next to the right front neckline. it is connected to the right front neckline.",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder seam.",
    "right shoulder seam": "The right shoulder seam is a point on the right shoulder, located on the edge of right shoulder. it connects the right back neckline and the outer top of right sleeve.",
    "outer top of right sleeve": "The outer top of right sleeve is a point on the outer side of the right sleeve, positioned on the top of right sleeve. it connects the right shoulder seam and the right sleeve, between the right shoulder seam and the outer upper point of right sleeve.",
    "outer upper point of right sleeve": "The outer upper point of right sleeve is the point on the outer side of the right sleeve, positioned between the outer top of right sleeve and the outer lower point of right sleeve.",
    "outer lower point of right sleeve": "The outer lower point of right sleeve is the point on the outer side of the right sleeve, positioned between the outer upper point of right sleeve and the outer bottom of right sleeve.",
    "outer bottom of right sleeve": "The outer bottom of right sleeve is the bottom point on the outer side of the right sleeve, positioned under the outer lower point of right sleeve. it is connected to outer lower point of right sleeve and the inner bottom of right sleeve.",
    "inner bottom of right sleeve": "The inner bottom of right sleeve is the bottom point on the inner side of the right sleeve, positioned under the inner lower point of right sleeve. it is connected to inner lower point of right sleeve and the outer bottom of right sleeve.",
    "inner lower point of right sleeve": "The inner lower point of right sleeve is the point on the inner side of the right sleeve, positioned between the inner upper point of right sleeve and the inner bottom of right sleeve.",
    "inner upper point of right sleeve": "The inner upper point of right sleeve is the point on the inner side of the right sleeve, positioned between the inner top of right sleeve and the inner lower point of right sleeve.",
    "inner top of right sleeve": "The inner top of right sleeve is a point on the inner side of the right sleeve, positioned on the top of right sleeve. it connects the right armpit and the right sleeve, between the right armpit and the inner upper point of right sleeve.",
    "right armpit": "The right armpit is a point connecting the right sleeve and the right side of body, located above top of right side seam.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the right armpit and the middle of right side seam, and connects them.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the bottom of right side seam, and connects them.",
    "bottom of right side seam": "The bottom of right side seam is bottom edge on the right side seam which means the line of right side of body. it is positioned under the middle of right side seam and right to the bottom of right placket.",
    "bottom of right placket": "The bottom of right placket is a point on the right placket and front of the clothes, positioned on the bottom edge of right placket, next to the bottom of right side seam, and under the lower point of right placket.",
    "bottom of left side seam": "The bottom of left side seam is bottom edge on the left side seam which means the line of left side of body. it is positioned under the middle of left side seam and left to the bottom of left placket.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the bottom of left side seam, and connects them.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the left armpit and the middle of left side seam, and connects them.",
    "left armpit": "The left armpit is a point connecting the left sleeve and the left side of body, located above top of left side seam.",
    "inner top of left sleeve": "The inner top of left sleeve is a point on the inner side of the left sleeve, positioned on the top of left sleeve. it connects the left armpit and the left sleeve, between the left armpit and the inner upper point of left sleeve.",
    "inner upper point of left sleeve": "The inner upper point of left sleeve is the point on the inner side of the left sleeve, positioned between the inner top of left sleeve and the inner lower point of left sleeve.",
    "inner lower point of left sleeve": "The inner lower point of left sleeve is the point on the inner side of the left sleeve, positioned between the inner upper point of left sleeve and the inner bottom of left sleeve.",
    "inner bottom of left sleeve": "The inner bottom of left sleeve is the bottom point on the inner side of the left sleeve, positioned under the inner lower point of left sleeve. it is connected to inner lower point of left sleeve and the outer bottom of left sleeve.",
    "outer bottom of left sleeve": "The outer bottom of left sleeve is the bottom point on the outer side of the left sleeve, positioned under the outer lower point of left sleeve. it is connected to outer lower point of left sleeve and the inner bottom of left sleeve.",
    "outer lower point of left sleeve": "The outer lower point of left sleeve is the point on the outer side of the left sleeve, positioned between the outer upper point of left sleeve and the outer bottom of left sleeve.",
    "outer upper point of left sleeve": "The outer upper point of left sleeve is the point on the outer side of the left sleeve, positioned between the outer top of left sleeve and the outer lower point of left sleeve.",
    "outer top of left sleeve": "The outer top of left sleeve is a point on the outer side of the left sleeve, positioned on the top of left sleeve. it connects the left shoulder seam and the left sleeve, between the left shoulder seam and the outer upper point of left sleeve.",
    "left shoulder seam": "The left shoulder seam is a point on the left shoulder, located on the edge of left shoulder. it connects the left back neckline and the outer top of left sleeve.",
    "top of left placket": "The top of left placket is a point on the left placket, positioned on the top edge of left placket and next to the left front neckline. it is connected to the left front neckline.",
    "upper point of left placket": "The upper point of left placket is a point on the left placket, positioned between the top of left placket and the lower point of left placket.",
    "lower point of left placket": "The lower point of left placket is a point on the left placket, positioned between the upper point of left placket and the bottom of left placket.",
    "bottom of left placket": "The bottom of left placket is a point on the left placket and front of the clothes, positioned on the bottom edge of left placket, next to the bottom of left side seam, and under the lower point of left placket.",
    "upper point of right placket": "The upper point of right placket is a point on the right placket, positioned between the top of right placket and the lower point of right placket.",
    "lower point of right placket": "The lower point of right placket is a point on the right placket, positioned between the upper point of right placket and the bottom of right placket.",
}


# 33 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!! + 추가 수정 진행(short sleeve shirt와 동일한 포인트는 동일한 설명)
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
long_sleeved_shirt = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder seam.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "center front neckline": "The center front neckline is the center point on the front side of neckline. it connects the right front necklines and left front necklines, located between the right and left front necklines.",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder seam.",
    "right shoulder seam": "The right shoulder seam is a point on the right shoulder, located on the edge of right shoulder. it connects the right back neckline and the outer top of right sleeve.",
    "outer top of right sleeve": "The outer top of right sleeve is a point on the outer side of the right sleeve, positioned on the top of right sleeve. it connects the right shoulder seam and the right sleeve, between the right shoulder seam and the outer upper point of right sleeve.",
    "outer upper point of right sleeve": "The outer upper point of right sleeve is the point on the outer side of the right sleeve, positioned between the outer top of right sleeve and the outer lower point of right sleeve.",
    "outer lower point of right sleeve": "The outer lower point of right sleeve is the point on the outer side of the right sleeve, positioned between the outer upper point of right sleeve and the outer bottom of right sleeve.",
    "outer bottom of right sleeve": "The outer bottom of right sleeve is the bottom point on the outer side of the right sleeve, positioned under the outer lower point of right sleeve. it is connected to outer lower point of right sleeve and the inner bottom of right sleeve.",
    "inner bottom of right sleeve": "The inner bottom of right sleeve is the bottom point on the inner side of the right sleeve, positioned under the inner lower point of right sleeve. it is connected to inner lower point of right sleeve and the outer bottom of right sleeve.",
    "inner lower point of right sleeve": "The inner lower point of right sleeve is the point on the inner side of the right sleeve, positioned between the inner upper point of right sleeve and the inner bottom of right sleeve.",
    "inner upper point of right sleeve": "The inner upper point of right sleeve is the point on the inner side of the right sleeve, positioned between the inner top of right sleeve and the inner lower point of right sleeve.",
    "inner top of right sleeve": "The inner top of right sleeve is a point on the inner side of the right sleeve, positioned on the top of right sleeve. it connects the right armpit and the right sleeve, between the right armpit and the inner upper point of right sleeve.",
    "right armpit": "The right armpit is a point connecting the right sleeve and the right side of body, located above the top of right side seam.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the right armpit and the middle of right side seam, and connects them.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the bottom of right side seam, and connects them.",
    "bottom of right side seam": "The bottom of right side seam is bottom edge on the right side seam which means the line of right side of body. it is positioned under the middle of right side seam and right to the center hem.",
    "center hem": "The center hem is the centeral point on the hem which means bottom edge of a piece of cloth, positioned between the bottom of right side seam and the bottom of left side seam.",
    "bottom of left side seam": "The bottom of left side seam is bottom edge on the left side seam which means the line of left side of body. it is positioned under the middle of left side seam and left to the center hem.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the bottom of left side seam, and connects them.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the left armpit and the middle of left side seam, and connects them.",
    "left armpit": "The left armpit is a point connecting the left sleeve and the left side of body, located above the top of left side seam.",
    "inner top of left sleeve": "The inner top of left sleeve is a point on the inner side of the left sleeve, positioned on the top of left sleeve. it connects the left armpit and the left sleeve, between the left armpit and the inner upper point of left sleeve.",
    "inner upper point of left sleeve": "The inner upper point of left sleeve is the point on the inner side of the left sleeve, positioned between the inner top of left sleeve and the inner lower point of left sleeve.",
    "inner lower point of left sleeve": "The inner lower point of left sleeve is the point on the inner side of the left sleeve, positioned between the inner upper point of left sleeve and the inner bottom of left sleeve.",
    "inner bottom of left sleeve": "The inner bottom of left sleeve is the bottom point on the inner side of the left sleeve, positioned under the inner lower point of left sleeve. it is connected to inner lower point of left sleeve and the outer bottom of left sleeve.",
    "outer bottom of left sleeve": "The outer bottom of left sleeve is the bottom point on the outer side of the left sleeve, positioned under the outer lower point of left sleeve. it is connected to outer lower point of left sleeve and the inner bottom of left sleeve.",
    "outer lower point of left sleeve": "The outer lower point of left sleeve is the point on the outer side of the left sleeve, positioned between the outer upper point of left sleeve and the outer bottom of left sleeve.",
    "outer upper point of left sleeve": "The outer upper point of left sleeve is the point on the outer side of the left sleeve, positioned between the outer top of left sleeve and the outer lower point of left sleeve.",
    "outer top of left sleeve": "The outer top of left sleeve is a point on the outer side of the left sleeve, positioned on the top of left sleeve. it connects the left shoulder seam and the left sleeve, between the left shoulder seam and the outer upper point of left sleeve.",
    "left shoulder seam": "The left shoulder seam is a point on the left shoulder, located on the edge of left shoulder. it connects the left back neckline and the outer top of left sleeve.",
}


# # 10 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
shorts = {
    "right waistband": "The right waistband is a point on the waistband that is on the top of short pants. it is the right edge of waistband, located on the right side of center waistband.",
    "center waistband": "The center waistband is a point on the waistband that is on the top of short pants. it is the centeral point of waistband, located between the right waistband and the left waistband.",
    "left waistband": "The left waistband is a point on the waistband that is on the top of short pants. it is the left edge of waistband, located on the left side of center waistband.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam, located at the center of right side seam and between right waistband and outer right hem.",
    "outer right hem": "The outer right hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the right corner of the right hem. it is under the middle of right side seam and next to the inner right hem.",
    "inner right hem": "The inner right hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the left corner of the right hem. it is under the crotch and next to the outer right hem.",
    "crotch": "The crotch is a point where two legs meet, connecting the inner right hem and the inner left hem. it is positioned near the center of hips.",
    "inner left hem": "The inner left hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the right corner of the left hem. it is under the crotch and next to the outer left hem.",
    "outer left hem": "The outer left hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the left corner of the left hem. it is under the middle of left side seam and next to the inner left hem.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam, located at the center of left side seam and between left waistband and outer left hem.",
}


# 29 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
short_sleeved_dress = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder seam.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "center front neckline": "The center front neckline is the center point on the front side of neckline. it connects the right front necklines and left front necklines, located between the right and left front necklines.",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder seam.",
    "right shoulder seam": "The right shoulder seam is a point on the right shoulder, located on the edge of right shoulder. it connects the right back neckline and the outer middle of right sleeve.",
    "outer middle of right sleeve": "The outer middle of right sleeve is the point on the outer side of the right sleeve, positioned between the right shoulder seam and the outer lower point of right sleeve.",
    "outer bottom of right sleeve": "The outer bottom of right sleeve is the bottom point on the outer side of the right sleeve, positioned under the outer middle of right sleeve. it is connected to outer middle of right sleeve and the inner bottom of right sleeve.",
    "inner bottom of right sleeve": "The inner bottom of right sleeve is the bottom point on the inner side of the right sleeve, positioned under the inner middle of right sleeve. it is connected to inner middle of right sleeve and the outer bottom of right sleeve.",
    "inner middle of right sleeve": "The inner middle of right sleeve is the point on the inner side of the right sleeve, positioned between the right armpit and the inner bottom of right sleeve.",
    "right armpit": "The right armpit is a point connecting the right sleeve and the right side of body, located above the top of right side seam.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the right armpit and the upper point of right side seam, and connects them.",
    "upper point of right side seam": "The upper point of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the middle of right side seam, and connects them.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the upper point of right side seam and the lower point of right side seam, and connects them.",
    "lower point of right side seam": "The lower point of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the middle of right side seam and the bottom of right side seam, and connects them.",
    "bottom of right side seam": "The bottom of right side seam is bottom edge on the right side seam which means the line of right side of body. it is positioned under the lower point of right side seam and right to the center hem.",
    "center hem": "The center hem is the centeral point on the hem which means bottom edge of a piece of cloth, positioned between the bottom of right side seam and the bottom of left side seam.",
    "bottom of left side seam": "The bottom of left side seam is bottom edge on the left side seam which means the line of left side of body. it is positioned under the lower point of left side seam and left to the center hem.",
    "lower point of left side seam": "The lower point of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the middle of left side seam and the bottom of left side seam, and connects them.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the upper point of left side seam and the lower point of left side seam, and connects them.",
    "upper point of left side seam": "The upper point of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the middle of left side seam, and connects them.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the left armpit and the upper point of left side seam, and connects them.",
    "left armpit": "The left armpit is a point connecting the left sleeve and the left side of body, located above the top of left side seam.",
    "inner middle of left sleeve": "The inner middle of left sleeve is the point on the inner side of the left sleeve, positioned between the left armpit and the inner bottom of left sleeve.",
    "inner bottom of left sleeve": "The inner bottom of left sleeve is the bottom point on the inner side of the left sleeve, positioned under the inner middle of left sleeve. it is connected to inner middle of left sleeve and the outer bottom of left sleeve.",
    "outer bottom of left sleeve": "The outer bottom of left sleeve is the bottom point on the outer side of the left sleeve, positioned under the outer middle of left sleeve. it is connected to outer middle of left sleeve and the inner bottom of left sleeve.",
    "outer middle of left sleeve": "The outer lower point of left sleeve is the point on the outer side of the left sleeve, positioned between the left shoulder seam and the outer bottom of left sleeve.",
    "left shoulder seam": "The left shoulder seam is a point on the left shoulder, located on the edge of left shoulder. it connects the left back neckline and the outer top of left sleeve.",
}


# 31 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
short_sleeved_outwear = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "top of right placket": "The top of right placket is a point on the right placket, positioned on the top edge of right placket and next to the right front neckline. it is connected to the right front neckline.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder seam.",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder seam.",
    "right shoulder seam": "The right shoulder seam is a point on the right shoulder, located on the edge of right shoulder. it connects the right back neckline and the outer middle of right sleeve.",
    "outer middle of right sleeve": "The outer middle of right sleeve is the point on the outer side of the right sleeve, positioned between the right shoulder seam and the outer lower point of right sleeve.",
    "outer bottom of right sleeve": "The outer bottom of right sleeve is the bottom point on the outer side of the right sleeve, positioned under the outer middle of right sleeve. it is connected to outer middle of right sleeve and the inner bottom of right sleeve.",
    "inner bottom of right sleeve": "The inner bottom of right sleeve is the bottom point on the inner side of the right sleeve, positioned under the inner middle of right sleeve. it is connected to inner middle of right sleeve and the outer bottom of right sleeve.",
    "inner middle of right sleeve": "The inner middle of right sleeve is the point on the inner side of the right sleeve, positioned between the right armpit and the inner bottom of right sleeve.",
    "right armpit": "The right armpit is a point connecting the right sleeve and the right side of body, located above the top of right side seam.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the right armpit and the middle of right side seam, and connects them.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the bottom of right side seam, and connects them.",
    "bottom of right side seam": "The bottom of right side seam is bottom edge on the right side seam which means the line of right side of body. it is positioned under the middle of right side seam and right to the bottom of right placket.",
    "bottom of right placket": "The bottom of right placket is a point on the right placket and front of the clothes, positioned on the bottom edge of right placket, next to the bottom of right side seam, and under the lower point of right placket.",
    "bottom of left side seam": "The bottom of left side seam is bottom edge on the left side seam which means the line of left side of body. it is positioned under the middle of left side seam and left to the bottom of left placket.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the bottom of left side seam, and connects them.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the left armpit and the middle of left side seam, and connects them.",
    "left armpit": "The left armpit is a point connecting the left sleeve and the left side of body, located above the top of left side seam.",
    "inner middle of left sleeve": "The inner middle of left sleeve is a point on the inner side of the left sleeve, positioned on the top of left sleeve. it connects the left armpit and the left sleeve, between the left armpit and the inner bottom of left sleeve.",
    "inner bottom of left sleeve": "The inner bottom of left sleeve is the bottom point on the inner side of the left sleeve, positioned under the inner middle of left sleeve. it is connected to inner bottom of left sleeve and the outer bottom of left sleeve.",
    "outer bottom of left sleeve": "The outer bottom of left sleeve is the bottom point on the outer side of the left sleeve, positioned under the outer middle of left sleeve. it is connected to inner bottom of left sleeve and the outer middle of left sleeve.",
    "outer middle of left sleeve": "The outer middle of left sleeve is the point on the outer side of the left sleeve, positioned between the left shoulder seam and the outer lower point of left sleeve.",
    "left shoulder seam": "The left shoulder seam is a point on the left shoulder, located on the edge of left shoulder. it connects the left back neckline and the outer middle of left sleeve.",
    "top of left placket": "The top of left placket is a point on the left placket, positioned on the top edge of left placket and next to the left front neckline. it is connected to the left front neckline.",
    "upper point of left placket": "The upper point of left placket is a point on the left placket, positioned between the top of left placket and the lower point of left placket.",
    "lower point of left placket": "The lower point of left placket is a point on the left placket, positioned between the upper point of left placket and the bottom of left placket.",
    "bottom of left placket": "The bottom of left placket is a point on the left placket and front of the clothes, positioned on the bottom edge of left placket, next to the bottom of left side seam, and under the lower point of left placket.",
    "upper point of right placket": "The upper point of right placket is a point on the right placket, positioned between the top of right placket and the lower point of right placket.",
    "lower point of right placket": "The lower point of right placket is a point on the right placket, positioned between the upper point of right placket and the bottom of right placket.",
}


# 25 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
short_sleeved_shirt = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder seam.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "center front neckline": "The center front neckline is the center point on the front side of neckline. it connects the right front necklines and left front necklines, located between the right and left front necklines.",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder seam.",
    "right shoulder seam": "The right shoulder seam is a point on the right shoulder, located on the edge of right shoulder. it connects the right back neckline and the outer top of right sleeve.",
    "outer middle of right sleeve": "The outer middle of right sleeve is the point on the outer side of the right sleeve, positioned between the right shoulder seam and the outer lower point of right sleeve.",
    "outer bottom of right sleeve": "The outer bottom of right sleeve is the bottom point on the outer side of the right sleeve, positioned under the outer middle of right sleeve. it is connected to outer middle of right sleeve and the inner bottom of right sleeve.",
    "inner bottom of right sleeve": "The inner bottom of right sleeve is the bottom point on the inner side of the right sleeve, positioned under the inner middle of right sleeve. it is connected to inner middle of right sleeve and the outer bottom of right sleeve.",
    "inner middle of right sleeve": "The inner middle of right sleeve is the point on the inner side of the right sleeve, positioned between the right armpit and the inner bottom of right sleeve.",
    "right armpit": "The right armpit is a point connecting the right sleeve and the right side of body, located above the top of right side seam.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the right armpit and the middle of right side seam, and connects them.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the bottom of right side seam, and connects them.",
    "bottom of right side seam": "The bottom of right side seam is bottom edge on the right side seam which means the line of right side of body. it is positioned under the middle of right side seam and right to the center hem.",
    "center hem": "The center hem is the centeral point on the hem which means bottom edge of a piece of cloth, positioned between the bottom of right side seam and the bottom of left side seam.",
    "bottom of left side seam": "The bottom of left side seam is bottom edge on the left side seam which means the line of left side of body. it is positioned under the middle of left side seam and left to the center hem.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the bottom of left side seam, and connects them.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the left armpit and the middle of left side seam, and connects them.",
    "left armpit": "The left armpit is a point connecting the left sleeve and the left side of body, located above the top of left side seam.",
    "inner middle of left sleeve": "The inner middle of left sleeve is a point on the inner side of the left sleeve, positioned on the top of left sleeve. it connects the left armpit and the left sleeve, between the left armpit and the inner bottom of left sleeve.",
    "inner bottom of left sleeve": "The inner bottom of left sleeve is the bottom point on the inner side of the left sleeve, positioned under the inner middle of left sleeve. it is connected to inner bottom of left sleeve and the outer bottom of left sleeve.",
    "outer bottom of left sleeve": "The outer bottom of left sleeve is the bottom point on the outer side of the left sleeve, positioned under the outer middle of left sleeve. it is connected to inner bottom of left sleeve and the outer middle of left sleeve.",
    "outer middle of left sleeve": "The outer middle of left sleeve is the point on the outer side of the left sleeve, positioned between the left shoulder seam and the outer lower point of left sleeve.",
    "left shoulder seam": "The left shoulder seam is a point on the left shoulder, located on the edge of left shoulder. it connects the left back neckline and the outer middle of left sleeve.",
}


# 8 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
skirt = {
    "right waistband": "The right waistband is a point on the waistband that is on the top of skirt. it is the right edge of waistband, located on the right side of center waistband.",
    "center waistband": "The center waistband is a point on the waistband that is on the top of skirt. it is the centeral point of waistband, located between the right waistband and the left waistband.",
    "left waistband": "The left waistband is a point on the waistband that is on the top of skirt. it is the left edge of waistband, located on the left side of center waistband.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam, located at the center of right side seam and between right waistband and outer right hem.",
    "bottom of right side seam": "The bottom of right side seam is a point on the bottom of the right seam, positioned at the right edge of hem which means bottom edge of a piece of cloth. it is on the right side of the center hem. it is under the middle of right side seam.",
    "center hem": "The center hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the center of hem. it is between the right hem and the left hem.",
    "bottom of left side seam": "The bottom of left side seam is a point on the bottom of the left seam, positioned at the left edge of hem which means bottom edge of a piece of cloth. it is on the left side of the center hem. it is under the middle of left side seam.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam, located at the center of left side seam and between left waistband and outer left hem.",
}


# 15 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
sling = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder strap.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "center front neckline": "The center front neckline is the center point on the front side of neckline. it connects the right front necklines and left front necklines, located between the right and left front necklines.",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder strap.",
    "right shoulder strap": "The right shoulder strap is a point on the right shoulder when a person wear the clothes, located on the tip of the right shoulder strap. it is connected to the right back neckline.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned above the middle of right side seam, especially under the right armpit.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the right hem.",
    "bottom of right side seam": "The bottom of right side seam is bottom point of the right side seam, positioned at the right edge of hem which means bottom edge of a piece of cloth. it is under the middle of right side seam.",
    "center hem": "The center hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the center of hem. it is between the bottom of right side seam and the bottom of left side seam.",
    "bottom of left side seam": "The bottom of left side seam is bottom point of the left side seam, positioned at the left edge of hem which means bottom edge of a piece of cloth. it is under the middle of left side seam.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the left hem.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned above the middle of left side seam, especially under the left armpit.",
    "left shoulder strap": "The left shoulder strap is a point on the left shoulder when a person wear the clothes, located on the tip of the left shoulder strap. it is connected to the left back neckline.",
}


# 19 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - Claude 3.5 기반 결과도 있으나 미완성!
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
sling_dress = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder strap.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "center front neckline": "The center front neckline is the center point on the front side of neckline. it connects the right front necklines and left front necklines, located between the right and left front necklines.",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder strap.",
    "right shoulder strap": "The right shoulder strap is a point on the right shoulder when a person wear the clothes, located on the tip of the right shoulder strap. it is connected to the right back neckline.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the right armpit and the upper point of right side seam, and connects them.",
    "upper point of right side seam": "The upper point of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the middle of right side seam, and connects them.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the upper point of right side seam and the lower point of right side seam, and connects them.",
    "lower point of right side seam": "The lower point of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the middle of right side seam and the bottom of right side seam, and connects them.",
    "bottom of right side seam": "The bottom of right side seam is bottom point of the right side seam, positioned at the right edge of hem which means bottom edge of a piece of cloth. it is under the middle of right side seam.",
    "center hem": "The center hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the center of hem. it is between the bottom of right side seam and the bottom of left side seam.",
    "bottom of left side seam": "The bottom of left side seam is bottom point of the left side seam, positioned at the left edge of hem which means bottom edge of a piece of cloth. it is under the middle of left side seam.",
    "lower point of left side seam": "The lower point of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the middle of left side seam and the bottom of left side seam, and connects them.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the upper point of left side seam and the lower point of left side seam, and connects them.",
    "upper point of left side seam": "The upper point of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the middle of left side seam, and connects them.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the left armpit and the upper point of left side seam, and connects them.",
    "left shoulder strap": "The left shoulder strap is a point on the left shoulder when a person wear the clothes, located on the tip of the left shoulder strap. it is connected to the left back neckline.",
}


# 14 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!! + 추가 수정 완료
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
trousers = {
    "right waistband": "The right waistband is a point on the waistband that is on the top of short pants. it is the right edge of waistband, located on the right side of center waistband.",
    "center waistband": "The center waistband is a point on the waistband that is on the top of short pants. it is the centeral point of waistband, located between the right waistband and the left waistband.",
    "left waistband": "The left waistband is a point on the waistband that is on the top of short pants. it is the left edge of waistband, located on the left side of center waistband.",
    "upper point of right outer side seam": "The upper point of right outer side seam is a point on the outer of right side seam, positioned under the right waistband and above the lower point of the right outer side seam.",
    "lower point of right outer side seam": "The lower point of right outer side seam is a point on the outer of right side seam, positioned under the upper point of the right outer side seam and above the outer right hem.",
    "outer right hem": "The outer right hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the right corner of the right hem. it is under the lower point of right side seam and next to the inner right hem.",
    "inner right hem": "The inner right hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the left corner of the right hem. it is under the crotch and next to the outer right hem.",
    "middle of right inner side seam": "The middle of right inner side seam is a point on the inner of right side seam, located between the crotch and inner right hem. specifically, it is positioned above the inner right hem and under the crotch.",
    "crotch": "The crotch is a point where two legs meet, connecting the inner right hem and the inner left hem. it is positioned near the center of hips and above the middle of right inner side seam.",
    "middle of left inner side seam": "The middle of left inner side seam is a point on the inner of left side seam, located between the crotch and inner left hem. specifically, it is positioned above the inner left hem and under the crotch.",
    "inner left hem": "The inner left hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the left corner of the left hem. it is under the crotch and next to the outer left hem.",
    "outer left hem": "The outer left hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the left corner of the left hem. it is under the lower point of left side seam and next to the inner left hem.",
    "lower point of left outer side seam": "The lower point of left outer side seam is a point on the outer of left side seam, positioned under the upper point of the left outer side seam and above the outer left hem.",
    "upper point of left outer side seam": "The upper point of left outer side seam is a point on the outer of left side seam, positioned under the left waistband and above the lower point of the left outer side seam.",
}


# 15 keypoints
# ANCHOR - 검수 완료!! + 추가 수정 완료
# REVIEW - left가 실제 left가 되도록 변경 완료!
# NOTE - 용어 통일화 작업 완료!
vest = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder seam.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "center front neckline": "The center front neckline is the center point on the front side of neckline. it connects the right front necklines and left front necklines, located between the right and left front necklines.",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder seam.",
    "right shoulder seam": "The right shoulder seam is a point on the right shoulder seam, located near the right shoulder and next to the right back neckline. it is connected to the right back neckline.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned above the middle of right side seam.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the bottom of right side seam.",
    "bottom of right side seam": "The bottom of right side seam is bottom edge on the right side seam which means the line of right side of body. it is positioned at the right edge of hem which means bottom edge of a piece of cloth and under the middle of right side seam and right to the center hem.",
    "center hem": "The center hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the center of hem. it is between the bottom of right side seam and the bottom of left side seam.",
    "bottom of left side seam": "The bottom of left side seam is bottom edge on the left side seam which means the line of left side of body. it is positioned at the left edge of hem which means bottom edge of a piece of cloth and under the middle of left side seam and left to the center hem.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the bottom of left side seam.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned above the middle of left side seam.",
    "left shoulder seam": "The left shoulder seam is a point on the left shoulder seam, located near the left shoulder and next to the left back neckline. it is connected to the left back neckline.",
}


# 19 keypoints
# NOTE - 직접 설명 수정 완료!
# ANCHOR - 검수 완료!!
# NOTE - 용어 통일화 작업 완료!
vest_dress = {
    "center back neckline": "The center back neckline is the center point on the rear side of neckline, located at the nape of the neck. it is also situated between the two points, left back neckline and right back neckline.",
    "right back neckline": "The right back neckline is a point on the back neckline, positioned at the right side of the center back neckline, connecting the center back neckline to the right shoulder seam.",
    "right front neckline": "The right front neckline is a point on the front neckline, located on the right side of the center front neckline, connecting the right back neckline and the center front neckline.",
    "center front neckline": "The center front neckline is the center point on the front side of neckline. it connects the right front necklines and left front necklines, located between the right and left front necklines.",
    "left front neckline": "The left front neckline is a point on the front neckline, located on the left side of the center front neckline, connecting the left back neckline and the center front neckline.",
    "left back neckline": "The left back neckline is a point on the back neckline, positioned at the left side of the center back neckline, connecting the center back neckline to the left shoulder seam.",
    "right shoulder seam": "The right shoulder seam is a point on the right shoulder seam, located near the right shoulder and next to the right back neckline. it is connected to the right back neckline.",
    "top of right side seam": "The top of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the right armpit and the upper point of right side seam, and connects them.",
    "upper point of right side seam": "The upper point of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the top of right side seam and the middle of right side seam. it is literally at upper than middle of right side seam.",
    "middle of right side seam": "The middle of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the upper point of right side seam and the lower point of right side seam, and connects them.",
    "lower point of right side seam": "The lower point of right side seam is a point on the right side seam which means the line of right side of body. it is positioned between the middle of right side seam and the bottom of right side seam. it is literally at lower than middle of right side seam.",
    "bottom of right side seam": "The bottom of right side seam is a point on the right side seam which means the line of right side of body, positioned at the right edge of hem which means bottom edge of a piece of cloth and under the lower point of right side seam and right to the center hem.",
    "center hem": "The center hem is a point on the hem which means bottom edge of a piece of cloth, positioned at the center of hem. it is between the bottom of right side seam and the bottom of left side seam.",
    "bottom of left side seam": "The bottom of left side seam is a point on the left side seam which means the line of left side of body, positioned at the left edge of hem which means bottom edge of a piece of cloth and under the lower point of left side seam and left to the center hem.",
    "lower point of left side seam": "The lower point of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the middle of left side seam and the bottom of left side seam. it is literally at lower than middle of left side seam.",
    "middle of left side seam": "The middle of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the upper point of left side seam and the lower point of left side seam, and connects them.",
    "upper point of left side seam": "The upper point of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the top of left side seam and the middle of left side seam. it is literally at upper than middle of left side seam.",
    "top of left side seam": "The top of left side seam is a point on the left side seam which means the line of left side of body. it is positioned between the left armpit and the upper point of left side seam, and connects them.",
    "left shoulder seam": "The left shoulder seam is a point on the left shoulder seam, located near the left shoulder and next to the left back neckline. it is connected to the left back neckline.",
}
