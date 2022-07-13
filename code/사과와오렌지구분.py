# 간단히 인공지능의 모델을 학습할 수 있는 티처블 머신을 이용하여 사과와 오렌지를 구분하는 모델 생성
# 특정 버전을 이용하는 가상환경 만들기

# conda create -n 가상환경이름 python=버전
# conda create -n 가상환경이름 python=버전 anaconda -y # 이렇게 깔면 기본 라이브러리도 같이 깔림
# conda search python # 설치 가능한 버전 확인
# python --version # 버전확인
# conda install -n 가상환경이름 설치할라이브러리 # 이렇게 하면 가상환경 진입 없이 가상환경에 라이브러리 설치 가능
# conda list # 가상환경 라이브러리 확인
# conda create -n 복사된가상환경이름 --clone 복사할가상환경이름
# conda remove -n 가상환경이름 --all -y # 가상환경 삭제

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

model_path = r".\converted_keras\keras_model.h5"
labels_path = r".\converted_keras\labels.txt"
image_path = r".\검증용사진\oranges-2533198_1920.jpg"

model = tensorflow.keras.models.load_model(model_path)

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

image = Image.open(image_path)
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array

prediction = model.predict(data)
print(prediction)

with open(labels_path, 'rt', encoding='UTF8') as f : 
    readLines = f.readlines()
    
if prediction[0,0] > prediction[0,1] :
    print(readLines[0])
else:
    print(readLines[1])
# ---------------------------------------------------------------------------------

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
from glob import glob

model_path = r".\converted_keras\keras_model.h5"
labels_path = r".\converted_keras\labels.txt"
img_list = glob(r'.\검증용사진\*.jpg')
img_list.extend(glob(r'.\검증용사진\*.png')) # 폴더의 png파일을 찾아 파일경로를 리스트에 추가

model = tensorflow.keras.models.load_model(model_path)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

for img_path in img_list:
    image = Image.open(img_path)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    print(prediction)

    with open(labels_path, 'rt', encoding='UTF8') as f : 
        readLines = f.readlines()
        
    if prediction[0,0] > prediction[0,1] :
        print(img_path,readLines[0])
    else:
        print(img_path,readLines[1])