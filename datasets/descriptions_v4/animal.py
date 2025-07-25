# AP-10K(17)
# NOTE - 34개의 category가 모두 동일한 keypoint definition을 따른다.
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left!
# antelope_body, beaver_body, bison_body, bobcat_body, cat_body, cheetah_body, cow_body, deer_body, dog_body, elephant_body, fox_body, giraffe_body, gorilla_body, hamster_body, hippo_body, horse_body, leopard_body, lion_body, otter_body, panda_body, panther_body, pig_body, polar_bear_body, rabbit_body, raccoon_body, rat_body, rhino_body, sheep_body, skunk_body, spider_monkey_body, squirrel_body, weasel_body, wolf_body, and zebra_body
animal_body = {
    "left eye": "The left eye is one of the two visual organs located on the face. It is positioned slightly to the left of the nose and just below the brow ridge, visible from the front.",
    "right eye": "The right eye is the visual organ located on the right side of the face. It is situated to the right of the nose and directly opposite the left eye.",
    "nose": "The nose is the central, protruding feature on the face, located just above the upper lip. It is positioned between and slightly below the eyes",
    "neck": "The neck is the part of the body connecting the head to the torso that refers to the area from the shoulders to the hip joints. It is located below the head, near the junction where the shoulders meet the body.",
    "root of tail": "The root of the tail is at the base of the spine, where the tail begins. It is located near the lower back, above the hips.",
    "left shoulder": "The left shoulder is the joint connecting the left arm to the torso. It is situated to the left of the neck and above the left elbow.",
    "left elbow": "The left elbow is the joint in the middle of the left arm, connecting the upper arm to the forearm. It is located between the left shoulder and the left front paw and connectd with them.",
    "left front paw": "The left front paw is the lower end of the left forelimb, used for movement and manipulation of objects. It is positioned below the left elbow and connected with the left elbow.",
    "right shoulder": "The right shoulder is the joint connecting the right arm to the torso. It is located to the right of the neck and above the right elbow.",
    "right elbow": "The right elbow is the joint in the middle of the right arm, connecting the upper arm to the forearm. It is situated between the right shoulder and the right front paw and connectd with them.",
    "right front paw": "The right front paw is the lower end of the right forelimb, used for movement and manipulation of objects. It is located below the right elbow and connectd with the right elbow.",
    "left hip": "The left hip is the joint connecting the left leg to the torso. It is positioned below the root of the tail and above the left knee.",
    "left knee": "The left knee is the joint in the middle of the left leg, connecting the upper leg to the lower leg. It is located between the left hip and the left back paw and connectd with them..",
    "left back paw": "The left back paw is the lower end of the left hind limb, used for movement and support. It is situated below the left knee.",
    "right hip": "The right hip is the joint connecting the right leg to the torso. It is positioned below the root of the tail and above the right knee.",
    "right knee": "The right knee is the joint in the middle of the right leg, connecting the upper leg to the lower leg. It is located between the right hip and the right back paw and connectd with them.",
    "right back paw": "The right back paw is the lower end of the right hind limb, used for movement and support. It is situated below the right knee."
}


# MacaquePose(17)
# human_body와 동일
# ANCHOR - 검수 완료!!
# REVIEW - left가 실제 left!
macaque_body = {
    "nose": "The nose is the central, protruding feature on the face, located just above the upper lip. It is positioned between and slightly below the eyes.",
    "left eye": "The left eye is one of the two visual organs located on the face. It is positioned slightly to the left of the nose and just below the brow ridge, visible from the front.",
    "right eye": "The right eye is the visual organ located on the right side of the face. It is situated to the right of the nose and directly opposite the left eye.",
    "left ear": "The left ear is located on the left side of the head, aligned with the eyes. It is situated to the left and slightly behind the left eye.",
    "right ear": "The right ear is located on the right side of the head, aligned with the eyes. It is situated to the right and slightly behind the right eye.",
    "left shoulder": "The left shoulder is the joint connecting the left arm to the torso. It is situated to the left of the neck and above the left elbow.",
    "right shoulder": "The right shoulder is the joint connecting the right arm to the torso. It is located to the right of the neck and above the right elbow.",
    "left elbow": "The left elbow is the joint in the middle of the left arm, connecting the upper arm to the forearm. It is located between the left shoulder and the left wrist.",
    "right elbow": "The right elbow is the joint in the middle of the right arm, connecting the upper arm to the forearm. It is situated between the right shoulder and the right wrist.",
    "left wrist": "The left wrist is the joint connecting the left forearm to the hand. It is positioned below the left elbow and above the left hand.",
    "right wrist": "The right wrist is the joint connecting the right forearm to the hand. It is located below the right elbow and above the right hand.",
    "left hip": "The left hip is the joint connecting the left leg to the torso. It is positioned below the lower back and above the left knee.",
    "right hip": "The right hip is the joint connecting the right leg to the torso. It is located below the lower back and above the right knee.",
    "left knee": "The left knee is the joint in the middle of the left leg, connecting the upper leg to the lower leg. It is situated between the left hip and the left ankle.",
    "right knee": "The right knee is the joint in the middle of the right leg, connecting the upper leg to the lower leg. It is positioned between the right hip and the right ankle.",
    "left ankle": "The left ankle is the joint connecting the left lower leg to the foot. It is located below the left knee.",
    "right ankle": "The right ankle is the joint connecting the right lower leg to the foot. It is situated below the right knee.",
}


# Vinegar Fly(32)
# NOTE - keypoint type 명칭을 바꿔야 함 => 명칭 그대로..마땅한 명칭이 없음
# ANCHOR - 검수 완료 및 수정 완료!!
# REVIEW - left가 실제 left!
# NOTE - 설명을 좀 더 직관적으로 수정
fly_body = {
    "head": "The head is the anterior part of the fly, located at the frontmost of the body, containing the eyes, antennae, and mouthparts.",
    "left eye": "The left eye is the visual organ on the left side of its head, located on the opposite side of the right eye.",
    "right eye": "The right eye is the visual organ on the right side of its head, located on the opposite side of the left eye.",
    "neck": "The neck is at the middle of the point where the head and thorax connect. it is positioned directly under the head and above the thorax.",
    "thorax": "The thorax is the central point of the body, located at the middle of the point where the neck and the abdomen connect.",
    "abdomen": "The abdomen is the bottom and posterior part of the body, located under the thorax, containing digestive and reproductive organs.",
    "first right foreleg": "The first right foreleg is the first segment of the right foreleg, attached to the thorax. it is positioned on the right upper side of the thorax and connects thorax and second right foreleg.",
    "second right foreleg": "The second right foreleg is the second segment of the right foreleg, positioned outside the first right foreleg and connects the first right foreleg and the third right foreleg.",
    "third right foreleg": "The third right foreleg is the third segment of the right foreleg, positioned outside the second right foreleg and connects the second right foreleg and the fourth right foreleg.",
    "fourth right foreleg": "The fourth right foreleg is the fourth segment of the right foreleg, positioned outside the third right foreleg and is connected to the third right foreleg.",
    "first right middle leg": "The first right middle leg is the first segment of the right middle leg, attached to the thorax. it is positioned on the right side of the thorax and connects thorax and the second right middle leg.",
    "second right middle leg": "The second right middle leg is the second segment of the right middle leg, positioned outside the first right middle leg and connects the first left middle leg and the third left middle leg.",
    "third right middle leg": "The third right middle leg is the third segment of the right middle leg, positioned outside the second right middle leg and connects the second left middle leg and the fourth left middle leg.",
    "fourth right middle leg": "The fourth right middle leg is the fourth segment of the right middle leg, positioned outside the third right middle leg and is connected to the third right middle leg.",
    "first right hindleg": "The first right hindleg is the first segment of the right hindleg, attached to the thorax. it is located on the lower right side of the thorax and connects thorax and second right hindleg.",
    "second right hindleg": "The second right hindleg is the second segment of the right hindleg, located outside the first right hindleg and connect the first right hindleg and the third right hindleg.",
    "third right hindleg": "The third right hindleg is the third segment of the right hindleg, located outside the second right hindleg and connect the second right hindleg and the fourth right hindleg.",
    "fourth right hindleg": "The fourth right hindleg is the fourth segment of the right hindleg, located outside the third right hindleg and is connected to the third right hindleg.",
    "first left foreleg": "The first left foreleg is the first segment of the left foreleg, attached to the thorax. it is positioned on the left upper side of the thorax and connects thorax and second left foreleg.",
    "second left foreleg": "The second left foreleg is the second segment of the left foreleg, positioned outside the first left foreleg and connects the first left foreleg and the third left foreleg.",
    "third left foreleg": "The third left foreleg is the third segment of the left foreleg, positioned outside the second left foreleg and connects the second left foreleg and the fourth left foreleg.",
    "fourth left foreleg": "The fourth left foreleg is the fourth segment of the left foreleg, positioned outside the third left foreleg and is connected to the third left foreleg.",
    "first left middle leg": "The first left middle leg is the first segment of the left middle leg, attached to the thorax. it is positioned on the left side of the thorax and connects thorax and the second left middle leg.",
    "second left middle leg": "The second left middle leg is the second segment of the left middle leg, positioned outside the first left middle leg and connects the first left middle leg and the third left middle leg.",
    "third left middle leg": "The third left middle leg is the third segment of the left middle leg, positioned outside the second left middle leg and connects the second left middle leg and the fourth left middle leg.",
    "fourth left middle leg": "The fourth left middle leg is the fourth segment of the left middle leg, positioned outside the third left middle leg and is connected to the third left middle leg.",
    "first left hindleg": "The first left hindleg is the first segment of the left hindleg, attached to the thorax. it is located on the lower left side of the thorax and connects thorax and second left hindleg.",
    "second left hindleg": "The second left hindleg is the second segment of the left hindleg, located outside the first left hindleg and connect the first left hindleg and the third left hindleg.",
    "third left hindleg": "The third left hindleg is the third segment of the left hindleg, located outside the second left hindleg and connect the second left hindleg and the fourth left hindleg.",
    "fourth left hindleg": "The fourth left hindleg is the fourth segment of the left hindleg, located outside the third left hindleg and is connected to the third left hindleg.",
    "left end of wing": "The left end of wing is the end point of the left wing. the left wing is attached to the left side of the thorax and this point is at the tip of the left wing.",
    "right end of wing": "The right end of wing is the end point of the right wing. the right wing is attached to the right side of the thorax and this point is at the tip of the right wing.",
}


# Desert Locust(35)
# NOTE - keypoint type 명칭을 바꿔야 함
# REVIEW - left가 실제 left!
# NOTE - 설명을 좀 더 직관적으로 수정
locust_body = {
    "head": "The head is the anterior part of the desert locust, containing the eyes, antennae, and mouthparts. it is at the frontmost point of this object.",
    "neck": "The neck is at the middle of the point where the head and thorax connect. it is positioned directly under the head and above the thorax.",
    "thorax": "The thorax is the central point of the body, located at the middle of the point where the neck and the abdomen connect.",
    "anterior abdomen": "The anterior abdomen is the anterior segment of the abdomen, located on the rear side of the thorax. it connects the thorax and the posterior abdomen.",
    "posterior abdomen": "The posterior abdomen is the posterior segment of the abdomen, extending from anterior abdomen. it is connected to anterior abdomen, positioned at the end of rear tip of this object.",
    "tip of left antenna": "The tip of left antenna is the outermost point of the left antenna on the head. it is connected to the base of left antenna.",
    "base of left antenna": "The base of left antenna is on left front of the head, connecting the head and the tip of left antenna.",
    "left eye": "The left eye is the point located on the left side of the head and on the opposite side of the right eye.",
    "first left foreleg": "The first left foreleg is the base of the left foreleg, attached to the thorax, connecting the thorax and the second left front leg.",
    "second left foreleg": "The second left foreleg is the second segment of the left foreleg, connecting the first left foreleg and the third left foreleg, located outside the first left foreleg.",
    "third left foreleg": "The third left foreleg is the third segment of the left foreleg, connecting the second left foreleg and the fourth left foreleg, located outside the second left foreleg.",
    "fourth left foreleg": "The fourth left foreleg is the fourth segment of the left foreleg and equal to the tip of the left foreleg, located outside the third left foreleg. it is connected to the third left foreleg.",
    "first left middle leg": "The first left middle leg is the first segment of the left middle leg, attached to the thorax. it is positioned on the left side of the thorax and connects thorax and the second left middle leg.",
    "second left middle leg": "The second left middle leg is the second segment of the left middle leg, positioned outside the first left middle leg and connects the first left middle leg and the third left middle leg.",
    "third left middle leg": "The third left middle leg is the third segment of the left middle leg, positioned outside the second left middle leg and connects the second left middle leg and the fourth left middle leg.",
    "fourth left middle leg": "The fourth left middle leg is the fourth segment of the left middle leg, positioned outside the third left middle leg and is connected to the third left middle leg.",
    "first left hindleg": "The first left hindleg is the first segment of the left hindleg, attached to the thorax. it is located on the lower left side of the thorax and connects thorax and second left hindleg.",
    "second left hindleg": "The second left hindleg is the second segment of the left hindleg, located outside the first left hindleg and connect the first left hindleg and the third left hindleg.",
    "third left hindleg": "The third left hindleg is the third segment of the left hindleg, located outside the second left hindleg and connect the second left hindleg and the fourth left hindleg.",
    "fourth left hindleg": "The fourth left hindleg is the fourth segment of the left hindleg, located outside the third left hindleg and is connected to the third left hindleg.",
    "tip of right antenna": "The tip of right antenna is the outermost point of the right antenna on the head. it is connected to the base of right antenna.",
    "base of right antenna": "The base of right antenna is on right front of the head, connecting the head and the tip of right antenna.",
    "right eye": "The right eye is the point located on the right side of the head and on the opposite side of the left eye.",
    "first right foreleg": "The first right foreleg is the base of the right foreleg, attached to the thorax, connecting the thorax and the second right front leg.",
    "second right foreleg": "The second right foreleg is the second segment of the right foreleg, connecting the first right foreleg and the third right foreleg, located outside the first right foreleg.",
    "third right foreleg": "The third right foreleg is the third segment of the right foreleg, connecting the second right foreleg and the fourth right foreleg, located outside the second right foreleg.",
    "fourth right foreleg": "The fourth right foreleg is the fourth segment of the right foreleg and equal to the tip of the right foreleg, located outside the third right foreleg. it is connected to the third right foreleg.",
    "first right middle leg": "The first right middle leg is the first segment of the right middle leg, attached to the thorax. it is positioned on the right side of the thorax and connects thorax and the second right middle leg.",
    "second right middle leg": "The second right middle leg is the second segment of the right middle leg, positioned outside the first right middle leg and connects the first left middle leg and the third left middle leg.",
    "third right middle leg": "The third right middle leg is the third segment of the right middle leg, positioned outside the second right middle leg and connects the second left middle leg and the fourth left middle leg.",
    "fourth right middle leg": "The fourth right middle leg is the fourth segment of the right middle leg, positioned outside the third right middle leg and is connected to the third right middle leg.",
    "first right hindleg": "The first right hindleg is the first segment of the right hindleg, attached to the thorax. it is located on the lower right side of the thorax and connects thorax and second right hindleg.",
    "second right hindleg": "The second right hindleg is the second segment of the right hindleg, located outside the first right hindleg and connect the first right hindleg and the third right hindleg.",
    "third right hindleg": "The third right hindleg is the third segment of the right hindleg, located outside the second right hindleg and connect the second right hindleg and the fourth right hindleg.",
    "fourth right hindleg": "The fourth right hindleg is the fourth segment of the right hindleg, located outside the third right hindleg and is connected to the third right hindleg.",
}

# AnimalWeb(9)
# NOTE - 30개의 category가 모두 동일한 keypoint definition을 따른다.
# alpaca_face, arcticwolf_face, bighornsheep_face, blackbuck_face, bonobo_face, californiansealion_face, camel_face, capebuffalo_face, capybara_face, chipmunk_face, commonwarthog_face, dassie_face, fallowdeer_face, fennecfox_face, ferret_face, gentoopenguin_face, gerbil_face, germanshepherddog_face, gibbons_face, goldenretriever_face, greyseal_face, grizzlybear_face, guanaco_face, klipspringer_face, olivebaboon_face, onager_face, pademelon_face, proboscismonkey_face, przewalskihorse_face, and quokka_face
# capex에서 발췌(https://github.com/matanr/capex/blob/main/models/datasets/datasets/mp100/utils.py)
# REVIEW - left가 실제 left로 변경 완료!
animal_face = {
    "top right side of the right eye": "The top right side of the right eye is located at the upper right corner of the animal's right eye. This point is at the start of the eyelid and below the eyebrow.",
    "bottom left side of the right eye": "The bottom left side of the right eye is located at the lower left corner of the animal's right eye. This point is at the end of the eyelid and below the eye.",
    "bottom right side of the left eye": "The bottom right side of the left eye is located at the lower right corner of the animal's left eye. This point is at the end of the eyelid and below the eye.",
    "top left side of the left eye": "The top left side of the left eye is located at the upper left corner of the animal's left eye. This point is at the start of the eyelid and below the eyebrow.",
    "nose tip": "The nose tip is the most protruding part in the center of the animal's face, located at the end of the nose. This point is between the eyes and above the lips, positioned on the middle of the nostril.",
    "right side of the lip": "The right side of the lip is located at the right end of the animal's lips. This point is below and to the right of the nose tip, at the right edge of the lips.",
    "left side of the lip": "The left side of the lip is located at the left end of the animal's lips. This point is below and to the left of the nose tip, at the left edge of the lips.",
    "top side of the lip": "The top side of the lip is located at the middle of the animal's upper lip. This point is directly below the nose tip and above the bottom side of the lip.",
    "bottom side of the lip": "The bottom side of the lip is located at the middle of the animal's lower lip. This point is directly below the top side of the lip."
}
