# Keypoint-5
# bed(10), chair(10), sofa(14), swivelchair(13), table(8)
# capex에서 발췌(https://github.com/matanr/capex/blob/main/models/datasets/datasets/mp100/utils.py)
# REVIEW - left가 실제 left가 되도록 변경 완료!

bed = {
    "bottom of right rear leg": "The bottom of right rear leg is at the bottom of the right rear leg, located under the right rear edge of the mattress and next to the bottom of left rear leg.",
    "bottom of right front leg": "The bottom of right front leg is at the bottom of the right front leg, located under the right front edge of the mattress and next to the bottom of left front leg.",
    "right rear edge of the mattress": "The right rear edge of the seat is at the right rear edge of the mattress, located above the bottom of right rear leg. it is at the bottom of headboard and next to the left rear edge of the mattress.",
    "right front edge of the mattress": "The right front edge of the seat is at the right front edge of the mattress, located above the bottom of right front leg. it is on the opposite location of the headboard and next to the left front edge of the mattress.",
    "right top edge of the headboard": "The right top edge of the headboard is one of the highest points in the bed, located at the right top edge of the headboard. it is next to the left top edge of the headboard.",
    "bottom of left rear leg": "The bottom of left rear leg is at the bottom of the left rear leg, located under the left rear edge of the mattress and next to the bottom of right rear leg.",
    "bottom of left front leg": "The bottom of left front leg is at the bottom of the left front leg, located under the left front edge of the mattress and next to the bottom of right front leg.",
    "left rear edge of the mattress": "The left rear edge of the seat is at the left rear edge of the mattress, located above the bottom of left rear leg. it is at the bottom of headboard and next to the right rear edge of the mattress.",
    "left front edge of the mattress": "The left front edge of the seat is at the left front edge of the mattress, located above the bottom of left front leg. it is on the opposite location of the headboard and next to the right front edge of the mattress.",
    "left top edge of the headboard": "The left top edge of the headboard is one of the highest points in the bed, located at the left top edge of the headboard. it is next to the right top edge of the headboard.",
}


chair = {
    "bottom of right front leg": "The bottom of right front leg is at the bottom of the right front leg, located under the right front edge of the seat and next to the bottom of left front leg.",
    "bottom of left front leg": "The bottom of left front leg is at the bottom of the left front leg, located under the left front edge of the seat and next to the bottom of right front leg.",
    "bottom of left rear leg": "The bottom of left rear leg is at the bottom of the left rear leg, located under the left rear edge of the seat and next to the bottom of right rear leg.",
    "bottom of right rear leg": "The bottom of right rear leg is at the bottom of the right rear leg, located under the right rear edge of the seat and next to the bottom of left rear leg.",
    "right front edge of the seat": "The right front edge of the seat is at the right front edge of the chair seat, located above the bottom of right front leg. it is on the opposite location of the backrest and next to the left front edge of the seat.",
    "left front edge of the seat": "The left front edge of the seat is at the left front edge of the chair seat, located above the bottom of left front leg. it is on the opposite location of the backrest and next to the right front edge of the seat.",
    "left rear edge of the seat": "The left rear edge of the seat is at the left rear edge of the chair seat, located above the bottom of left rear leg. it is at the bottom of backrest and next to the right rear edge of the seat.",
    "right rear edge of the seat": "The right rear edge of the seat is at the right rear edge of the chair seat, located above the bottom of right rear leg. it is at the bottom of backrest and next to the left rear edge of the seat.",
    "right top edge of the backrest": "The right top edge of the backrest is one of the highest points in the chair, located at the right top edge of the backrest. it is next to the left top edge of the backrest.",
    "left top edge of the backrest": "The left top edge of the backrest is one of the highest points in the chair, located at the left top edge of the backrest. it is next to the right top edge of the backrest.",
}

sofa = {
    "bottom of right rear leg": "The bottom of right rear leg is at the bottom of the right rear leg, located under the right rear edge of the seat and next to the bottom of left rear leg.",
    "bottom of right front leg": "The bottom of right front leg is at the bottom of the right front leg, located under the right front edge of the seat and next to the bottom of left front leg.",
    "right rear edge of the seat": "The right rear edge of the seat is at the right rear edge of the sofa seat, located above the bottom of right rear leg. it is at the bottom of backrest and next to the left rear edge of the seat.",
    "right front edge of the seat": "The right front edge of the seat is at the right front edge of the sofa seat, located above the bottom of right front leg. it is on the opposite location of the backrest and next to the left front edge of the seat.",
    "rear edge of the right armrest": "The rear edge of the right armrest is at the rear edge of the right armrest of sofa, located at the junction of the right armrest and the backrest. it is behind the front edge of the right armrest and under the right top edge of the backrest.",
    "front edge of the right armrest": "The front edge of the right armrest is at the front edge of the right armrest of sofa, located in front of the rear edge of the right armrest. it is at the higher position than the seat.",
    "right top edge of the backrest": "The right top edge of the backrest is one of the highest points in the sofa, located at the right top edge of the backrest. it is next to the left top edge of the backrest and above the rear edge of the right armrest.",
    "bottom of left rear leg": "The bottom of left rear leg is at the bottom of the left rear leg, located under the left rear edge of the seat and next to the bottom of right rear leg.",
    "bottom of left front leg": "The bottom of left front leg is at the bottom of the left front leg, located under the left front edge of the seat and next to the bottom of right front leg.",
    "left rear edge of the seat": "The left rear edge of the seat is at the left rear edge of the sofa seat, located above the bottom of left rear leg. it is at the bottom of backrest and on opposite position of the right rear edge of the seat.",
    "left front edge of the seat": "The left front edge of the seat is at the left front edge of the sofa seat, located above the bottom of left front leg. it is on the opposite location of the backrest and next to the right front edge of the seat.",
    "rear edge of the left armrest": "The rear edge of the left armrest is at the rear edge of the left armrest of sofa, located at the junction of the left armrest and the backrest. it is behind the front edge of the left armrest and under the left top edge of the backrest.",
    "front edge of the left armrest": "The front edge of the left armrest is at the front edge of the left armrest of sofa, located in front of the rear edge of the left armrest. it is at the higher position than the seat.",
    "left top edge of the backrest": "The left top edge of the backrest is one of the highest points in the sofa, located at the left top edge of the backrest. it is next to the right top edge of the backrest and above the rear edge of the left armrest.",
}


# NOTE - wheel 중복,
# NOTE - 앉는 곳을 기준으로 오른쪽 앞부터 뒤쪽을 돌아 반대편 앞다리까지 1~5번 포인트를 형성한다. => 반영 완료!
# NOTE - 애매모호한, 상상해야하는 내용 배제
swivelchair = {
    "front wheel": "The front wheel is at the base of chair, located on the right front of the chair seat, so that it is around the foot when a person sits down. so it is usually next to the fifth wheel and in front of the second wheel.",
    "second wheel": "The second wheel is at the base of chair, located usually at the right side of the chair seat. this wheel is located behind the first wheel and in front of the third wheel. at the same time, it is on the opposite side of the fourth wheel.",
    "third wheel": "The third wheel is at the base of chair, positioned on the rear of the seat. this wheel is located between the second wheel and the fourth wheel.",
    "fourth wheel": "The fourth wheel is at the base of chair, situated usually at the left side of the seat. it is between the third wheel and the fifth wheel and on the opposite side of the second wheel.",
    "fifth wheel": "The fifth wheel is at the base of chair, located on the left front of the seat, when a person sitting on the chair. it is next to the first wheel and in front of the fourth wheel.",
    "bottom of chair column": "The bottom of chair column is above the wheel center and at the bottom of the column that connects the chair seat and the wheels. all wheels are met and connected at this point, located higher than the wheel.",
    "top of chair column": "The top of chair column is under the seat and at the top of the column that connects the chair seat and the wheels. thus, it is above the bottom of chair column.",
    "right front edge of the seat": "The right front edge of the seat is at the right front edge of the seat. it is at the opposite side of the left front edge of the seat and in front of the right rear edge of the seat.",
    "left front edge of the seat": "The left front edge of the seat is at the left front edge of the seat. it is at the opposite location of the right front edge of the seat and in front of the left rear edge of the seat.",
    "left rear edge of the seat": "The left rear edge of the seat is at the left rear edge of the seat. it is at the opposite side of the right rear edge of the seat and behind the left front edge of the seat.",
    "right rear edge of the seat": "The right rear edge of the seat is at the right rear edge of the seat. it is at the opposite side of the left rear edge of the seat and behind the right front edge of the seat.",
    "right top edge of the backrest": "The right top edge of the backrest is one of the highest points in the chair, located at the right top edge of the backrest. it is next to the left top edge of the backrest.",
    "left top edge of the backrest": "The left top edge of the backrest is one of the highest points in the chair, located at the left top edge of the backrest. it is next to the right top edge of the backrest.",
}


# FIXME - 이미지별로 상판의 라벨링 순서가 뒤죽박죽
table = {
    "left and front side of the top": "The left and front side of the top is the front-left corner of the table's surface, where the left edge meets the front edge. It's typically the closest point to someone approaching the table from the left side.",
    "left and back side of the top": "The left and back side of the top is the rear-left corner of the table's surface, opposite to the front-left corner. This point is usually closest to the wall if the table is placed against one.",
    "right and front side of the top": "The right and front side of the top is the front-right corner of the table's surface, diagonally opposite to the left and back corner. It's usually the point closest to someone approaching the table from the right side.",
    "right and back side of the top": "The right and back side of the top is the rear-right corner of the table's surface, diagonally opposite to the left and front corner. This is typically the farthest point from someone sitting at the front of the table.",
    "left and front leg": "The left and front leg is the support structure at the front-left corner of the table, connecting the top surface to the floor. It's one of the four main points of contact with the ground.",
    "left and back leg": "The left and back leg is the support structure at the rear-left corner of the table, opposite to the left and front leg. It provides stability to the back-left portion of the table.",
    "right and front leg": "The right and front leg is the support structure at the front-right corner of the table, diagonally opposite to the left and back leg. It's one of the first visible legs when approaching the table from the right.",
    "right and back leg": "The right and back leg is the support structure at the rear-right corner of the table, diagonally opposite to the left and front leg. It's typically the leg farthest from someone sitting at the front of the table."
}
