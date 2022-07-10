# openCV를 이용하여 사진에서 얼굴을 찾고 찾은 얼굴부분을 모자이크 처리
# pip install opencv-python

import numpy as np
import cv2

# 얼굴과 눈을 찾기위한 openCV 알고리즘이 적용된 파일 불러옴
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

ff = np.fromfile('\샘플사진.jpg', np.uint8) # 한글을 읽지 못하여 영어로 불러옴
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED) # imdecode 하여 numpy이미지파일을 opencv로 불러옴
img = cv2.resize(img, dsize=(0,0), fx=1, fy=1.0, interpolation=cv2.INTER_LINEAR) # 이미지 크기를 조절. fx, fy비율로 조절
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 얼굴을 찾기 위해 회색조 처리

faces = face_cascade.detecMultiScale(gray,1.2,5)
for (x,y,w,h) in faces: # 얼굴을 찾아 파란색으로 네모표시함
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detecMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes: # 눈을 찾아 녹색네모로 표시
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# -----------------------------------------------------------------------------------------

# 사진 속 얼굴을 모자이크 처리하는 코드 만들기

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

ff = np.fromfile('\샘플사진.jpg', np.uint8) # 한글을 읽지 못하여 영어로 불러옴
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED) # imdecode 하여 numpy이미지파일을 opencv로 불러옴
img = cv2.resize(img, dsize=(0,0), fx=1, fy=1.0, interpolation=cv2.INTER_LINEAR) # 이미지 크기를 조절. fx, fy비율로 조절
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 얼굴을 찾기 위해 회색조 처리


faces = face_cascade.detectMultiScale(gray,1.2,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detecMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes: # 눈을 찾아 녹색네모로 표시
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),2)

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
