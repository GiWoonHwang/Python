# openCV를 이용하여 사진에 효과르 넣어 그림처럼 보이게 하는 프로그램 만들어 보기
# pip install opencv-python

import numpy as np
import cv2

ff = np.fromfile(r'\.여행사진.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0,0), fx =1.0, fy = 1.0, interpolation=cv2.INTER_LINEAR) 

cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.1)   # 사진을 그림으로 변환함

cv2.imshow('cartoon view', cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ---------------------------------------------------------------------------------------------

# 시그마 값에 따라 사진이 변환되는것을 실시간으로 보는 코드

import numpy as np
import cv2

ff = np.fromfile(r'.\여행사진.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

def onChange(pos):
    pass

cv2.namedWindow("Trackbar Windows") # 트랙 윈도우 생성

cv2.createTrackbar("sigma_s", "Trackbar Windows", 0, 200, onChange) # 트랙의 최소 최댓값 설정, 트랙이 움직일 때 마다 동작하는 함수 지정
cv2.createTrackbar("sigma_r", "Trackbar Windows", 0, 100, onChange)

cv2.setTrackbarPos("sigma_s", "Trackbar Windows", 100)
cv2.setTrackbarPos("sigma_r", "Trackbar Windows", 10)

while True:
    
    if cv2.waitKey(100) == ord('q'): # OpenCV에서 킷값을 입력받는다. 100ms동안 킷값을 기다리다가 값이 없으면 timeout으로 코드를 종료하고 다음 코드를 실행, q의 킷값이 입력되면 break로 while문 종료
        break
    
    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") / 100.0

    print("sigma_s_value:",sigma_s_value)
    print("sigma_r_value:",sigma_r_value)

    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)  # 이미지를 그림화한다.

    cv2.imshow("Trackbar Windows", cartoon_img)

cv2.destroyAllWindows() 