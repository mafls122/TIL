import cv2, dlib
import numpy as np
from imutils import face_utils
# 얼굴에서 눈 검출하기

# 눈 사이즈
IMG_SIZE = (34, 26)

# 얼굴 검출 : dlib 사용
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# 눈 자르기
def crop_eye(img, eye_points):
  x1, y1 = np.amin(eye_points, axis=0)
  x2, y2 = np.amax(eye_points, axis=0)
  cx, cy = (x1 + x2) / 2, (y1 + y2) / 2

  w = (x2 - x1) * 1.2
  h = w * IMG_SIZE[1] / IMG_SIZE[0]

  margin_x, margin_y = w / 2, h / 2

  min_x, min_y = int(cx - margin_x), int(cy - margin_y)
  max_x, max_y = int(cx + margin_x), int(cy + margin_y)

  eye_rect = np.rint([min_x, min_y, max_x, max_y]).astype(np.int)

  eye_img = gray[eye_rect[1]:eye_rect[3], eye_rect[0]:eye_rect[2]]

  return eye_img, eye_rect

# 캠 로드
cap = cv2.VideoCapture(0)

while cap.isOpened():
  ret, img = cap.read()

  if not ret:
    break

  # 흑백 변환
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # 얼굴 검출
  faces = detector(gray)

  for face in faces:
    shapes = predictor(gray, face)
    shapes = face_utils.shape_to_np(shapes)

    eye_img_l, eye_rect_l = crop_eye(gray, eye_points=shapes[36:42])
    eye_img_r, eye_rect_r = crop_eye(gray, eye_points=shapes[42:48])

    eye_img_l = cv2.resize(eye_img_l, dsize=IMG_SIZE)
    eye_img_r = cv2.resize(eye_img_r, dsize=IMG_SIZE)
    
    # 각각 보여주기
    cv2.imshow('l', eye_img_l)
    cv2.imshow('r', eye_img_r)
 
    # 눈 네모 그리기
    cv2.rectangle(img, pt1=tuple(eye_rect_l[0:2]), pt2=tuple(eye_rect_l[2:4]), color=(0, 0, 0), thickness=2)
    cv2.rectangle(img, pt1=tuple(eye_rect_r[0:2]), pt2=tuple(eye_rect_r[2:4]), color=(255, 255, 255), thickness=2)

  cv2.imshow('result', img)
  
  if cv2.waitKey(1) == ord('q'):
    break
