# pip install torch==1.9.0
# pip install torchvision==0.10.0

# from glob import glob

# img_path = r'.\원본이미지'

# # 파일의 경로를 리스트로 반환
# img_list = glob(img_path + '\*.jpg')
# img_list.extend(glob(img_path + '\*.png'))

# print(img_list)

# -------------------------------------------------------------------------------------------------

# 파이토치를 이용해 사진 폴더에서 특정 사진을 찾는 코드 만들기

# import torch
# from glob import glob

# img_path = r'.\원본이미지'

# img_list = glob(img_path + '\*.jpg')
# img_list.extend(glob(img_path + '\*.png'))

# print(img_list)

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# for img_path in img_list:
#     results = model(img_path) # 이미지에서 사람, 물건등을 찾아 반환
#     print(img_path)
#     results.save(r".\이미지확인용") # 저장
#     for pred in results.pred[0]:
#         tag = results.names[int(pred[-1])] 
#         print(tag)
# -------------------------------------------------------------------------------------------------

# 사람이 있는 사진,그림을 찾아 특정 폴더로 이동시킴
import torch
from glob import glob
import shutil # 파일 이동을 위한 라이브러리
import os # os 관련 라이브러리 

img_path = r'.\원본이미지'

img_list = glob(img_path + '\*.jpg')
img_list.extend(glob(img_path + '\*.png'))

print(img_list)

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img_move_path = r'.\사람만분류'

for img_path in img_list:
    results = model(img_path)
    print(img_path)
    for pred in results.pred[0]:
        tag = results.names[int(pred[-1])] 
        print(tag)
        if tag == "person": # 사람이 있으면 조건이 참
            print("move")
            shutil.move(img_path, img_move_path + '\\' + os.path.basename(img_path)) # 파일 이동(파일,목적지)
            break