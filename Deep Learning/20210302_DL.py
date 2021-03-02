# dlib 사용하여 얼굴 인식하기
from imutils import face_utils
import numpy as np
import imutils
import dlib
import cv2
import time

# 얼굴 인식 표시
def show_raw_detection(image, detector, predictor):
    # 이미지 흑백으로 변경
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 흑백이미지 얼굴 검출
    rects = detector(gray, 1)

    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # 얼굴검출 좌표, 네모 그리기
        # (x, y, w, h) = face_utils.rect_to_bb(rect)
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # 얼굴 68개 점 찍기
        for (x, y) in shape:
            cv2.circle(image, (x, y), 1, (0, 0, 255), -1)


if __name__ == '__main__':

    detector = dlib.get_frontal_face_detector()  # 정면 얼굴 검출기
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  # 학습된 랜드마크 모델 : 눈,코,입,턱 등 68개의 점이 학습됨

    # 캠 로드
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        show_raw_detection(frame, detector, predictor)
        if not ret:
            break

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) == ord('q'):
            break




