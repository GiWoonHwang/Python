# 기본지식
# 기존 데이터를 이용해 앞으로의 일을 예측하는 머신러닝
# 머신러닝 안에 여러 알고리즘이 있는데 이중 가장 좋은 효과를 내는 것이 딥 러닝이다
# 인공지능 > 머신러닝 > 딥 러닝 
# 이름표가 주어진 데이터를 이용해 이름표를 맞히는 것을 지도학습 , 공톡적 특징을 찾아내 그룹으로 분류하는것을 비지도 학습
#현대의 시스템은 딥 러닝 응용 프로그램, 대규모 병렬 처리, 고사양 3D 게이밍, 기타 까다로운 워크로드 등을 비롯하여 그 어느 때보다도 많은 작업을 수행해야 합니다. 중앙 처리 장치(CPU)와 그래픽 처리 장치(GPU)의 역할은 매우 다릅니다. CPU는 어느 용도로 사용됩니까? GPU는 어느 용도로 사용됩니까? 새로운 컴퓨터를 구매하고 사양을 비교할 때 각각의 역할을 아는 것이 중요합니다.

# CPU란 무엇입니까?
# 수백만 개의 트랜지스터로 구축된 CPU는 여러 개의 프로세싱 코어를 갖추고 있으며 보통 컴퓨터의 뇌로 간주됩니다. CPU는 컴퓨터 및 운영 체제에 필요한 명령과 처리를 실행하므로 모든 현대 컴퓨팅 시스템에 필수적인 요소입니다. 또한, CPU는 웹 서핑에서 스프레드시트 제작에 이르는 프로그램의 실행 속도를 결정하는 데도 중요하게 작용합니다.

# GPU란 무엇입니까?
# GPU는 더 작고 보다 전문화된 코어로 구성된 프로세서입니다. 여러 개의 코어가 함께 작동하므로, 여러 코어로 나누어 처리할 수 있는 작업의 경우 GPU가 엄청난 성능 이점을 제공합니다.

# CPU와 GPU의 차이점은 무엇입니까?
# CPU와 GPU는 서로 공통점이 많습니다. 둘 다 아주 중요한 컴퓨팅 엔진입니다. 둘 다 실리콘 기반 마이크로프로세서입니다. 그리고 둘 다 데이터를 처리합니다. 하지만 CPU와 GPU는 아키텍처가 다르며 만들어진 용도가 다릅니다.

# CPU는 다양한 워크로드, 특히 대기 시간이나 코어당 성능이 중요한 워크로드에 적합합니다. CPU는 강력한 실행 엔진으로서 코어 수가 적으며 개별적인 작업과 신속한 작업 처리에 이러한 코어를 집중합니다. 이 때문에 연속적인 컴퓨팅이나 데이터베이스 실행과 같은 작업에 적합합니다.

# GPU는 특정 3D 렌더링 작업 속도를 단축하기 위해 개발된 전문 ASIC로 시작했습니다. 시간이 지나면서 이러한 고정된 기능의 엔진의 프로그래밍이 더욱더 수월해졌으며 융통성도 높아졌습니다. GPU의 주요 기능은 여전히 최신 인기 게임의 그래픽과 점점 생생해지는 비주얼이긴 하지만, 최근에는 범용적인 병렬 프로세서로도 발전하여 점점 더 다양한 응용 프로그램을 처리하고 있습니다.

# 통합 그래픽이란 무엇입니까?
# 통합 또는 공유 그래픽은 CPU와 동일한 칩에 탑재됩니다. 특정 CPU에는 전용 또는 개별 그래픽을 사용할 필요가 없도록 GPU가 내장되기도 합니다. 또한, IGP라고도 불리는 통합 그래픽 프로세서는 CPU와 메모리를 공유합니다.

# 통합 그래픽 프로세서는 여러 이점을 제공합니다. 이러한 그래픽 프로세서는 CPU와 통합으로 전용 그래픽 프로세서를 사용할 때보다 공간, 비용 및 에너지 효율이 높아집니다.  통합 그래픽 프로세서는 그래픽 관련 데이터 처리와 웹 탐색, 4K 영화 스트리밍, 캐주얼 게이밍과 같은 일반적인 작업 수행에 필요한 강력한 성능을 제공합니다.

# 이러한 접근 방식은 노트북, 태블릿, 스마트폰 및 일부 데스크탑과 같이 작은 크기와 에너지 효율이 중요한 장치에 가장 많이 채택됩니다.

# 딥 러닝 및 AI 가속화
# 현대에는 딥 러닝 및 인공 지능(AI)와 같이 점점 더 많은 워크로드가 GPU에서 실행됩니다. 여러 개의 신경망 계층 또는 2D 이미지와 같은 대규모의 특정 데이터 세트에 대한 딥 러닝 훈련에는 GPU 또는 기타 가속기가 적합합니다.

# 딥 러닝 알고리즘은 GPU 가속화 접근 방식을 채택하도록 발전했으며, 이를 통해 성능이 크게 향상되고 여러 가지 실제 문제에 대한 훈련을 최초로 실용적이고 실행 가능한 범위로 맞출 수 있게 되었습니다.

# 시간의 흐름에 따라 CPU와 CPU에서 실행되는 소프트웨어 라이브러리는 딥 러닝 작업을 더욱 원활하게 수행할 수 있도록 발전했습니다. 예를 들어, CPU 기반 시스템은 폭넓은 소프트웨어 최적화 및 최신 인텔® 제온® 스케일러블 프로세서에 탑재되는 인텔® 딥 러닝 부스트(인텔® DL Boost)와 같은 전용 AI 하드웨어 추가를 통해 향상된 딥 러닝 성능을 제공하게 되었습니다.

# 언어, 문자 및 시계열 데이터에 대한 고해상도, 3D 및 비이미지 기반 딥 러닝과 같은 다양한 응용 프로그램의 경우 CPU가 우수한 성능을 제공합니다. CPU는 현대의 그 어떤 GPU와도 비교할 수 없는 많은 메모리 용량을 지원하여 복잡한 모델 또는 딥 러닝 응용 프로그램(예: 2D 이미지 감지)에 필요한 성능을 제공합니다.

# CPU와 GPU의 조합, 거기에 충분한 RAM을 더하면 딥 러닝 및 AI에 알맞은 테스트베드를 구축할 수 있습니다.

# 수십 년간 CPU 개발 분야를 선두해온 리더십
# 인텔은 1971년 단일 칩에 완전히 통합된 최초의 상용 마이크로프로세서인 4004를 도입한 이래로 CPU 혁신을 위한 오랜 역사를 쌓아왔습니다.

# 오늘날에는 인텔® CPU을 통해 잘 알려진 x86 아키텍처에서 사용자가 원하는 AI를 원하는 위치에 구축할 수 있습니다. 데이터 센터 및 클라우드에서의 고성능 인텔® 제온® 스케일러블 프로세서에서 에지에서의 전력 효율적인 인텔® 코어™에 이르기까지, 인텔은 모든 요구 사항에 맞는 CPU를 제공합니다.

# 11세대 인텔® 코어™ 프로세서의 지능적인 성능
# 11세대 인텔® 코어™ 프로세서는 인텔의 고급 프로세스 기술, 재설계된 코어 아키텍처, 완전히 새로워진 그래픽 아키텍처 및 내장 AI 지침을 활용하여 최적화된 성능과 경험을 지능적으로 제공합니다.

# 11세대 인텔® 코어™ 프로세서 기반 시스템에는 최신 통합 인텔® Iris® Xe 그래픽이 탑재됩니다. 또한, 울트라 씬 노트북과 같은 특정 폼 팩터 장치에도 인텔 Xe 아키텍처를 기반으로 하는 최초의 개별 그래픽 처리 장치(GPU)가 포함됩니다. 인텔® Iris® Xe MAX 전용 그래픽을 통해 얇고 가벼운 노트북에서 콘텐츠 제작 및 게이밍 향상을 위해 더욱 개선된 성능과 새로운 기능을 비롯한 혁신적인 발전을 경험할 수 있습니다.

# 인텔® Iris® Xe 그래픽에는 인텔® 딥 러닝 부스트 기반 AI가 탑재되어 더욱 우수한 콘텐츠 제작과 사진 및 비디오 편집을 경험할 수 있으며, 더욱 우수한 배터리 수명을 위한 저전력 아키텍처로 설계 작업 및 멀티태스킹을 보다 원활하게 수행할 수 있습니다.

# 인텔 개별 GPU
# 인텔은 인텔 Xe 아키텍처를 기반으로 하는 두 개의 개별 GPU 옵션을 제공합니다.

# 인텔® Iris® Xe MAX 그래픽은 인텔 Xe 아키텍처를 기반으로 한 얇고 가벼운 노트북을 위해 개발된 최초의 개별 그래픽 처리 장치(GPU)입니다. 11세대 인텔® 코어™ 프로세서와 함께 작동되도록 최적화되어 향상된 콘텐츠 제작 및 게임을 위한 더 많은 성능과 새로운 기능을 제공합니다.

# 인텔® 서버 GPU는 새로운 인텔 Xe 아키텍처를 기반으로 하는 데이터 센터를 위한 개별 그래픽 처리 장치입니다. 기하급수적인 확장을 위해 설계된 인텔® 서버 GPU는 Android 게이밍, 미디어 트랜스코딩/인코딩, OTT(over-the-top) 비디오 스트리밍 시 새로운 차원의 경험을 선사합니다.

# 현대에는 CPU와 GPU의 성능을 비교하는 것은 무의미합니다. 다양한 컴퓨팅 요구 사항을 충족하기 위해서는 두 처리 장치를 조합하는 것이 그 어느 때보다도 중요합니다. 최적의 결과는 해당 작업에 적합한 도구를 사용할 때 비로소 얻을 수 있습니다.

# 딥러닝 작업 환경 만들기. 1. 컴퓨터에 필요한 프로그램을 성치, 2. 구글코랩을 이용(구글코랩이란 주피터 노트북 환경을 구글 클라우드에 마련해 놓은 것 but 원하는 패키지 매번 설치, 작업중이던 데이터 잃어버릴 수 있음)
# 파이썬 설치, 딥러닝을 작동시키는 대표적인 언어, 아나콘다 설치, 우리가 사용해야 하는 여러 모듈을 모아둔곳 추가로 텐서플로, 케라스 

# 순서 1. conda create -n py37 python=3.7 2.conda activate py37 3. pip install tensorflow==2.0, pip install keras==2.3, pip install jupyter 3. jupyter notebook




# # -*- coding: utf-8 -*- 환경이 잘 구성 되었는지 테스트 해보는 코드
# # 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

# # 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

# # 필요한 라이브러리를 불러옵니다.
# import numpy as np
# import tensorflow as tf

# # 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분입니다.
# np.random.seed(3)
# tf.random.set_seed(3)

# # 준비된 수술 환자 데이터를 불러들입니다.
# Data_set = np.loadtxt("../dataset/ThoraricSurgery.csv", delimiter=",")

# # 환자의 기록과 수술 결과를 X와 Y로 구분하여 저장합니다.
# X = Data_set[:,0:17]
# Y = Data_set[:,17]

# # 딥러닝 구조를 결정합니다(모델을 설정하고 실행하는 부분입니다).
# model = Sequential()
# model.add(Dense(30, input_dim=17, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))

# # 딥러닝을 실행합니다.
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# model.fit(X, Y, epochs=100, batch_size=10)


# # 미지의 일을 예측하는 원리 : 수술하기 전에 수술 후의 생존율을 수치로 예측할 방법은 ?
# #  생존율을 정리해 놓은 데이털르 머신러닝 알고리즘에 넣는다 여기서 데이터가 입력되고 패턴이 분석되는 과정을 '학습' 이라고 한다.
# # 학습과정을 다시 말하면 깨끗한 좌표평면에 기존 환자들을 하나씩 배치하는 과정이다

# # 딥러닝을 구동하는데 필요한 케라스 함수 호출
# from tensorflow.keras.models import Sequential #순차
# from tensorflow.keras.layers import Dense # 밀집

# # 필요한 라이브러리 블러오기
# import numpy as np
# import tensorflow as tf

# # 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분
# np.random.seed(3)
# tf.random.set_seed(3)

# # 준비된 수술 환자 데이터를 불러오기
# Data_set = np.loadtxt("../dataset/ThoraricSurgery.csv", delimiter=",")

# # 환자의 기록과 수술 결과를 x와 y로 구분하여 저장
# x = Data_set[:,0:17]
# y = Data_set[:,17]

# # 딥러닝 구조를 결정(모델을 설정하고 실행)
# model = Sequential()
# model.add(Dense(30, input_dim=17, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))

# # 딥러닝 실행
# model.compile(loss='binary_crossentropy', optimizer='adam',
# metrics=['accuracy'])
# model.fit(x,y,epochs=100, batch_size=10)

# csv 파일의 1-17은 속성 18번은 클래스 라고 한다 앞서 언급한 이름표라고 하지요
# 속성만을 담는 데이터 셋과 ,클래스만을 담는 데이터 셋 만들어줘야 한다
# 텐서플로는 목적지까지 빠르게 이동시켜주는 비행기, 케라스는 도착을 책임지는 파일럿에 비유 가능
# sequential() 딥러닝 구조를 한층한층 쉽게 쌓아올릴 수 있게 해줌 그 후 model.add() 함루를 사용해 필요한 층 추가
# dense는 각 층이 어떠한 특성을 가질지 옵션 설정

# activation 다음 층으로 값을 어떻게 넘길지 결정하는 함수, 여기서는 relu()와 sigodi() 함수를 사용하게 끔 지정

# 딥러닝은 통계의 결과들이 무수히 얽히고 설켜 이루어지는 복잡한 연산의 결정체, 딥러닝을 이해하기 위해선 가장 밑단에서 이루어지는 
# 두가지 계산 원리를 알아야 한다. 바로 선형회귀와 로지스틱 회귀이다

# 1. 선형회귀 : 쉽게말하면 선긋기 이다. ex) 학생들의 중간고사 성적이 () 에 따라 다르다
# 성적을 변하게 하는 요소 '정보' 를 x라고 하고 그 값에 따라 변하는 성적을 y로 하자
# 여기서 x는 독립적으로 변할 수 있기 떄문에 '독립변수' 라고 한다
# y는 독립변수에 따라 변하기 때문에 종속변수 라고한다 x값이 하나일때는 단순 선형 회귀,
# 여러개일 때는 다중 선형 회귀 라고 한다
# 선형 회귀란 임의의 직선을 그어 이에 대한 평균 오차를 구하고 ,이 값을 가장 작게 만들어주는 a와 b를 찾아가는 작업


# 코딩으로 최소 제곱법을 구현해보자

# import numpy as np

# x = [2,4,6,8]
# y = [81,93,91,97]

# mx = np.mean(x) # 원소의 평균을 구한다
# my = np.mean(y)
# print(x)
# print(y)

# # x의 각 원소와 x의 평균값들의 차를 제곱하라 분모부분이다
# divisor = sum([(i- mx)**2 for i in x])

# # x와 y의 편차를 곱해서 합한 값 d의 초깃값을 으로 설정한 뒤 x의 개수만큼 실행 후 최소 제곱법 실행
# def top(x,mx,y,my):
#     d = 0
#     for i in range(len(x)):
#         d += (x[i]-mx) * (y[i]-my)
#     return d
# dividend = top(x,mx,y,my)

# print(divisor)
# print(dividend)

# # 기울기
# a = dividend / divisor
# b = my- (mx*a)
      
# print(a)
# print(b)

# import numpy as np

# #기울기 a와 y절편 b
# fake_a_b = [3,76]

# #x,y의 데이터 값
# data = [[2,81],[4,93],[6,91],[8,97]]
# x = [i[0] for i in data]
# y = [i[1] for i in data]

# # y = ax+b에 a와 b의 값을 대입하여 결과를 출력하는 함수
# def predict(x):
#     return fake_a_b[0]*x + fake_a_b[1]

# # mse 함수, 평균제곱오차를 구하는 식 이다
# def mse(y,y_hat):
#     return ((y-y_hat)**2).mean()

# # mse함수를 각 y값에 대입하여 최종 값을 구하는 함수
# def mse_val(y, predict_result):
#     return mse(np.array(y), np.array(predict_result))

# # 예측 값이 들어갈 빈 리스트
# predict_result = []

# # 모든 x값을 한번씩 대입하여
# for i in range(len(x)):
#     # predict_result 를 완성
#     predict_result.append(predict(x[i]))
#     print("공부한시간 =%.f, 실제점수=%.f, 예측점수=%.f" % (x[i],y[i],predict(x[i])))
    
# # 최종 mse 함수 출력
# print("최종값:" + str(mse_val(predict_result,y)))

# 경사 하강법 : 그래프의 오차를 비교하여 가장 작은 방향으로 이동시킨다. 미분의 기울기를 이용하는 경사 하강법 이다
# 오차가 가장 적은 최솟값 m의 순간 기울기는 평행한선 즉 0이다. 따라서 우린 미분값이 0인 지점을 찾는 것
# 다음과 같은 과정을 거친다
# 1. a1에서 미분한다. 2. 구해진 기울기의 반대방향으로 얼마간 이동시킨 a2에서 미분을 구한다. 3. 위에서 구한 미분값이 0이 아니면 위 과정을 반복한다 4. 결국 기울기가 0인 한점으로 수렴한다
# 여기서 학습률이란 이동거리를 정해준다 학습률을 찾는것은 중요한 최적화 과정 중 하나이다.

# # 경사 하강법 실습
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # 공부시간 x와 성적y 의 리스트 만들기
# data = [[2,81],[4,93],[6,91],[8,97]]
# x = [i[0] for i in data]
# y = [i[1] for i in data]

# # 그래프로 나타내기
# plt.figure(figsize=(8,5))
# plt.scatter(x,y)
# plt.show()

# #리스트로 되어 있는 x와 y값을 넘파이 배열로 바꾹(인덱스를 주어 하나씩 불러와 계산이 가능하게 하기 위함)
# x_data = np.array(x)
# y_data = np.array(y)

# # 기울기 a와 절편 b의 값 초기화
# a = 0
# b = 0

# # 학습률 정하기
# lr = 0.03

# # 몇번 반복될지 설정
# epochs = 2001

# # 경사 하강법 시작
# for i in range(epochs):# 에포크 수 만큼 반복한다
#     y_pred = a * x_data + b # y를 구하는 식 세우기
#     error = y_data - y_pred # 오차를 구하는 식

#     # 오차 함수를 a로 미분한 값
#     a_diff = -(2/len(x_data)) * sum(x_data * (error))
#     # 오차 함수를 b로 미분한 값
#     b_diff = -(2/len(y_data)) * sum(error)

#     a = a - lr * a_diff # 학습률을 곱해 기존의 값 업데이트
#     b = b - lr * b_diff 

#     if i % 100 == 0: # 100번 반복될 때마다 현재의 a값, b값 출력
#         print("epochs=%.f, 기울기=%.f, 절편=%.04f" % (i,a,b))

# # 앞서 구한 기울기와 절편을 이용해 그래프를 다시 그리기
# y_pred = a * x_data + b
# plt.scatter(x,y)
# plt.plot([min(x_data),max(x_data)],[min(y_pred),max(y_pred)])
# plt.show()

# 다중선현 회귀. x변수를 늘려주는거임 y = a1x1 + a2x2 +b 
# 다중 선형 회귀 실습

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d

# # 공부시간 x와 성적 y의 리스트 만들기
# data = [[2,0,81],[4,4,93],[6,2,91],[8,3,97]]
# x1 = [i[0] for i in data]
# x2 = [i[1] for i in data]
# y = [i[2] for i in data]

# # 그래프로 확인
# ax = plt.axes(projection='3d')
# ax.set_xlabel('study_hours')
# ax.set_ylabel('private_calss')
# ax.set_zlabel("Score")
# ax.dist = 11
# ax.scatter(x1,x2,y)
# plt.show()

# # 리스트로 되어 있는 x와 y 값을 넘파이 배열로 바꾸기(인덱스로 하나씩 불러와 계산할 수 있도록 하기 위함이다)
# x1_data = np.array(x1)
# x2_data  = np.array(x2)
# y_data = np.array(y)

# # 기울기 a와 절편 b의 값 초기화
# a1 = 0 
# a2 = 0
# b = 0

# # 학습률
# lr = 0.02

# # 몇번 반복할지 설정한다. (0부터 세기 때문에 원하는 반복 횟수에 +1)
# epochs = 2001

# # 경사 하강법을 시작
# for i in range(epochs): # 변수 수 만큼 반복
#     y_pred = a1 * x1_data + a2 * x2_data + b # y를 구하는 식 세우기
#     error = y_data - y_pred # 오차를 구하는 식이다
#     # 오차함수를 a1으로 미분함 값
#     a1_diff = -(2/len(x1_data)) * sum(x1_data *(error))
#     # 오차함수를 a2로 미분한 값
#     a2_diff = -(2/len(x1_data)) * sum(x1_data*(error))
#     # 오차함수를 b로 미분한 값
#     b_diff = -(2/len(x1_data)) * sum(y_data - y_pred)
#     a1 = a1 - lr * a1_diff #학습률을 곱해 기존의 a1값 업데이트
#     a2 = a2 -lr * a2_diff
#     b = b *lr * b_diff
    
#     if i % 100 ==0: #100번 반복될 때마다 현재의 a,a2,b값 출력
#         print(a1,a2,b)

#로지스틱 회귀 : 참과 거짓중 하나의 값을 내놓는다. 참,거짓 미니 판단 장치를 만들어 주어진 입력 값의 특징 추출하고 이를 통해 모델을 만든다
# 이를 통해 누군가 비슷한 질문을 하면 지금까지 만들어놓은 모델을 꺼내어 답을 한다
# 로지스틱 회귀 역시 적절한 선을 그리는 작업이지만 참거짓이기 때문에 s자형태 곡선을 그린다
# ax + b a가 커질주록 경사는 커진다 b는 좌우이동을 나타냄 또 a값이 작아지면 오차는 무한대로 커진다


# 로지스틱 회귀
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # 공부 시간 x와 합격 여부 y의 리스트 만들기
# data = [[2,0],[4,0],[6,0],[8,1],[10,1],[12,1],[14,1]]

# x_data = [i[0] for i in data]
# y_data = [i[1] for i in data]

# #그래프로 나타내기
# plt.scatter(x_data, y_data)
# plt.xlim(0,15)
# plt.ylim(-.1,1.1)

# # 기울기와 a와 절편 b의 값 초기화
# a = 0
# b = 0

# # 학습률
# lr = 0.05

# #  시그모이드 함수 정의
# def sigmoid(x) :
#     return 1 / (1 + np.e **(-x))

# #경사하강법 실행
# for i in range(2001):
#     for x_data, y_data in data:
#         a_diff = x_data *(sigmoid(a*x_data + b)-y_data)
#         b_diff = sigmoid(a*x_data + b ) - y_data
#         a = a - lr * a_diff
#         b = b - lr * b_diff
#         if i % 1000 == 0 :
#             print(i,a,b)
            
#     #앞서 구한 기울기와 절편을 이용해 그래프 그리기
#     plt.scatter(x_data, y_data)
#     plt.xlim(0,15)
#     plt.ylim(-.1,1.1)
#     x_range = (np.arange(0,15,0.1)) # 그래프로 나타낼 x값의 범위 정하기
#     plt.plot(np.arange(0,15,0.1),np.array([sigmoid(a*x+b) 
# for x in x_range]))
#     plt.show()

# 퍼셉트론 : 신경망의 가장 기본적인 단위이다 퍼셉트론만으로는 xor 문제를 해결하지못했지만, 다층 퍼셉트론의 등장으로 해결
# 다층 퍼셉트론이란 중간에 은닉층을 둬 좌표평면을 왜곡시키는것
# 가운데 숨어있는 은닉층으로 퍼셉트론이 각각 자신의 가중치와 바이어스값을 보내고 이 은닉층에서
# 모인 값이 한 번더 시그모이드 함수를 이용해 최종값으로 결과를 보냄

# 다층 퍼셉트론으로 xor 문제 해결하기
# import numpy as np
# from numpy.lib import stride_tricks

# # 가중치와 바이어스

# w11 = np.array([-2,-2])
# w12 = np.array([2,2])
# w2 = np.array([1,1])
# b1 =3 
# b2 = -1
# b3 = -1

# #퍼셉트론
# def MLP(x,w,b) :
#     y = np.sum(w*x) +b
#     if y <= 0 :
#         return 0
#     else:
#         return 1

# # NAND 게이트
# def NAND(x1,x2):
#     return MLP(np.array([x1,x2]),w11,b1)

# # OR 게이트
# def OR(x1,x2):
#     return MLP(np.array([x1,x2]),w12,b2)

# # AND 게이트

# def AND(x1,x2):
#     return  MLP(np.array([x1,x2]), w2,b3)

# # XOR 게이트
# def XOR(x1,x2):
#     return AND(NAND(x1,x2),OR(x1,x2))

# # x1,x2 값을 번갈아 가며 입력하여 최종값 출력
# if __name__ == '__main__':
#     for x in [(0,0),(1,0),(0,1),(1,1)]:
#         y = XOR(x[0],x[1])
#         print(str(x))
#         print(str(y))   

# # 인디언 당뇨병 예측
# #!/usr/bin/env python

# # -*- coding: utf-8 -*-
# # 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

# # pandas 라이브러리를 불러옵니다.
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # 피마 인디언 당뇨병 데이터셋을 불러옵니다. 불러올 때 각 컬럼에 해당하는 이름을 지정합니다.
# df = pd.read_csv('../../dataset/pima-indians-diabetes.csv',
#                names = ["pregnant", "plasma", "pressure", "thickness", "insulin", "BMI", "pedigree", "age", "class"])

# # 처음 5줄을 봅니다.
# print(df.head(5))

# # 데이터의 전반적인 정보를 확인해 봅니다.
# print(df.info())

# # 각 정보별 특징을 좀더 자세히 출력합니다.
# print(df.describe())

# # 데이터 중 임신 정보와 클래스 만을 출력해 봅니다.
# print(df[['plasma', 'class']])

# # 데이터 간의 상관관계를 그래프로 표현해 봅니다.

# colormap = plt.cm.gist_heat   #그래프의 색상 구성을 정합니다.
# plt.figure(figsize=(12,12))   #그래프의 크기를 정합니다.

# # 그래프의 속성을 결정합니다. vmax의 값을 0.5로 지정해 0.5에 가까울 수록 밝은 색으로 표시되게 합니다.
# sns.heatmap(df.corr(),linewidths=0.1,vmax=0.5, cmap=colormap, linecolor='white', annot=True)
# plt.show()

# grid = sns.FacetGrid(df, col='class')
# grid.map(plt.hist, 'plasma',  bins=10)
# plt.show()

# # 딥러닝을 구동하는 데 필요한 케라스 함수를 불러옵니다.
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

# # 필요한 라이브러리를 불러옵니다.
# import numpy
# import tensorflow as tf

# # 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분입니다.
# numpy.random.seed(3)
# tf.random.set_seed(3)

# # 데이터를 불러 옵니다.
# dataset = numpy.loadtxt("../dataset/pima-indians-diabetes.csv", delimiter=",")
# X = dataset[:,0:8]
# Y = dataset[:,8]

# # 모델을 설정합니다.
# model = Sequential()
# model.add(Dense(12, input_dim=8, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(1, activation='sigmoid'))

# # 모델을 컴파일합니다.
# model.compile(loss='binary_crossentropy',
#              optimizer='adam',
#              metrics=['accuracy'])

# # 모델을 실행합니다.
# model.fit(X, Y, epochs=200, batch_size=10)

# # 결과를 출력합니다.
# print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))


# print(df[['pregnant','class']].groupby(['pregnant'], 
# as_index=False).mean().sort_values(by='pregnant',ascending=True))

# 다중 분류 문제 해결하기
# 아이리스란 꽃의 품종은 매우 비슷하다. 딥러닝을 통해 이것을 구분할 수 있을까 ?
# csv파일 속성을 보았더니 클래스가 3개이다. 이것을 '다중분류' 라고 한다. 

# 먼저 일부 데이터를 불러와 내용을 본다  그 후 pairplot() 함수를 써서 그래프 전체를 본다 
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# df = pd.read_csv('../dataset/iris.csv', names = ["sepal_length","sepal_width","petal_length","petal_width","species"])
# print(df.head())
# sns.pairplot(df,hue='species');
# plt.show


# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# from sklearn.preprocessing import LabelEncoder

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np
# import tensorflow as tf

# # 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분입니다.
# np.random.seed(3)
# tf.random.set_seed(3)

# # 데이터 입력
# df = pd.read_csv('../dataset/iris.csv', names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

# # 그래프로 확인
# sns.pairplot(df, hue='species');
# plt.show()

# # 데이터 분류
# dataset = df.values
# X = dataset[:,0:4].astype(float)
# Y_obj = dataset[:,4]

# # 문자열을 숫자로 변환
# e = LabelEncoder()
# e.fit(Y_obj)
# Y = e.transform(Y_obj)
# Y_encoded = tf.keras.utils.to_categorical(Y)

# # 모델의 설정
# model = Sequential()
# model.add(Dense(16,  input_dim=4, activation='relu'))
# model.add(Dense(3, activation='softmax'))

# # 모델 컴파일
# model.compile(loss='categorical_crossentropy',
#             optimizer='adam',
#             metrics=['accuracy'])

# # 모델 실행
# model.fit(X, Y_encoded, epochs=50, batch_size=1)

# # 결과 출력
# print("\n Accuracy: %.4f" % (model.evaluate(X, Y_encoded)[1]))

# 과적합 피하기

from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import numpy
import tensorflow as tf

# seed 값 설정
numpy.random.seed(3)
tf.random.set_seed(3)

# 데이터 입력
df = pd.read_csv('../dataset/sonar.csv', header=None)
'''
# 데이터 개괄 보기
print(df.info())

# 데이터의 일부분 미리 보기
print(df.head())
'''
dataset = df.values
X = dataset[:,0:60]
Y_obj = dataset[:,60]

# 문자열 변환
e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)

# 모델 설정
model = Sequential()
model.add(Dense(24,  input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(loss='mean_squared_error',
            optimizer='adam',
            metrics=['accuracy'])

# 모델 실행
model.fit(X, Y, epochs=200, batch_size=5)

# 결과 출력
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))

# 실행결과 정확도가 100이 나왔다. 정말로 정확도가 100일까 ?
# 과적합이란 학습 데이터셋 안에서는 일정 수준 이상의 예측 정확도를 보이지만 새로운 데이터에 적응하면 잘 맞지 않는것을 말한다.

#과적합을 방지해보자
# 1. 100개의 샘플이있다면 70개는 학습셋으로 30개는 테스트셋으로
# 2. 초기 저장된 70개를 모델이라고 한다. 따라서 나머지 30개의 샘플로 실험해서 정확도를 살펴보면 학습이 얼마나 잘 되어 있는지 알 수 있다.
# 그런데 우리는 지금까지 테스트셋 없이 학습해 왔다. 그런데도 매번 정확도를 계산 할 수 있었다 . 왜그럴까 ? 우리는 지금까지 학습 데이터를 이용해 
# 정확도를 측정어한것은 데이터에 들어있는 모든 샘플을 그대로 테스트에 활용한 결과이다.
# 그러나 머신러닝의 최종 목적은  과거의 데이터를 토대로 새로운 데이터를 예측하는것.
# 즉 새로운 데이터에 사용할 모델을 만드는 것이 최종 목적이므로 테스트셋을 만들어 정확한 평가를 병행해야함
# 학습셋만 가지고 평가할때, 층을 더하거나 에포크 값을 높여 횟수를 늘리면 정확도가 올라갈 수 있다 그러나 학습데이터셋으로만
# 평가한 데이터가 테스트셋에서도 그대로 나타나지 않는다. 즉 과적합이 발생하는것 

# 학습셋과 테스트셋을 구분해서 딥러닝을 해보자
from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

df = pd.read_csv('../dataset/sonar.csv', header=None)

'''
print(df.info())
print(df.head())
'''

dataset = df.values
X = dataset[:,0:60]
Y_obj = dataset[:,60]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)

# 학습 셋과 테스트 셋의 구분
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

model = Sequential()
model.add(Dense(24,  input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
            optimizer='adam',
            metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=130, batch_size=5)

# 테스트셋에 모델 적용
print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))

# 모델 저장과 재사용
from keras.models import Sequential, load_model
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder

import pandas as pd
import numpy
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

df = pd.read_csv('../dataset/sonar.csv', header=None)
'''
print(df.info())
print(df.head())
'''
dataset = df.values
X = dataset[:,0:60]
Y_obj = dataset[:,60]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)
# 학습셋과 테스트셋을 나눔
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

model = Sequential()
model.add(Dense(24,  input_dim=60, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
            optimizer='adam',
            metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=130, batch_size=5)
model.save('my_model.h5')  # 모델을 컴퓨터에 저장

del model       # 테스트를 위해 메모리 내의 모델을 삭제
model = load_model('my_model.h5') # 모델을 새로 불러옴

print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))  # 불러온 모델로 테스트 실행

#K겹 교차 검증
# 테스트를 정확하게 설정할수록 세상으로 나왔을 때 더 잘 작동한다고 할 수있다. 하지만 데이터가 충분하지 않을때, 문제가 발생한다
#앞서 가지고 있는 데이터의 약 70%를 학습셋으로 써야 했으므로 테스트셋은 겨우 30%이다 이러한 단점을 보안하고자 나온것이 K교차 검증이다
#데이터셋을 여러개로 나누어 하니씩 테스트셋으로 사용하고 나머지를 모두 합해서 학습셋으로 사용하는 방법이다.
#이렇게 하면 데이터의 전부를 테스트셋으로 사용 가능하다

#데이터를 원하는 숫자만큼 쪼개서 학습셋과 테스트셋으로 사용하게 만드는 함수이다

from sklearn.model_selection import StratifiedkFold
n_fold = 10 # 파일을 10개로 쪼갠다
skf = StratifiedkFold(n_split=n_foldm shuffle=True, random_state=seed)

# 그런다음 모델을 만들고 실행하는 부분을 for 구문으로 묶어 n_fold만큼 반복되게 한다  전체 코드를 보자

from keras.models import Sequential
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold

import numpy
import pandas as pd
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

df = pd.read_csv('../dataset/sonar.csv', header=None)

dataset = df.values
X = dataset[:,0:60]
Y_obj = dataset[:,60]

e = LabelEncoder()
e.fit(Y_obj)
Y = e.transform(Y_obj)

# 10개의 파일로 쪼갬
n_fold = 10
skf = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)

# 빈 accuracy 배열
accuracy = []

# 모델의 설정, 컴파일, 실행
for train, test in skf.split(X, Y):
    model = Sequential()
    model.add(Dense(24, input_dim=60, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='mean_squared_error',
                  optimizer='adam',
                  metrics=['accuracy'])
    model.fit(X[train], Y[train], epochs=100, batch_size=5)
    k_accuracy = "%.4f" % (model.evaluate(X[test], Y[test])[1]) # 정확도를 매번 저장하여 한번에 보여줄수있게 . accuracy배열을 만든다
    accuracy.append(k_accuracy)

# 결과 출력
print("\n %.f fold accuracy:" % n_fold, accuracy)

# 베스트 모델 만들기
# 레드와잉과 화이트와인 데이터를 합친 후 , 구분하는 실험 진행

rom keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping

import pandas as pd
import numpy
import tensorflow as tf
import matplotlib.pyplot as plt

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# 데이터 입력
df_pre = pd.read_csv('../dataset/wine.csv', header=None)
df = df_pre.sample(frac=1)  # sample함수는 원본 데이터에서 정해진 비율만큼 랜덤으로 뽑아오는 함수이다 frac=1 이라고 놓으면 원본데이터를 100퍼 불러 올 수 있다.

dataset = df.values
X = dataset[:,0:12] # 파이썬은 숫자를 1부터 세지 않고 0부터 센다. 범위를 정할 경우 콜론앞의 숫자는 범위의 맨 청므을 뜻하고, 콜론 뒤의 숫자는 이숫자 '바로 앞'이 범위의 마지막이라는 것이다.
Y = dataset[:,12]

# 모델 설정
model = Sequential()
model.add(Dense(30,  input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#모델 컴파일
model.compile(loss='binary_crossentropy',
           optimizer='adam',
           metrics=['accuracy'])

# 모델 실행
model.fit(X, Y, epochs=200, batch_size=200)

# 결과 출력
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))

#모델을 업데이트 해보자 모델을 그냥 저장하는것이 아니라 에포크마다 모델의 정확도를 함께 기록하면서 저장해보자
# 1. 모델이 저장될 폴더를 지정하자
# 2. 에포크 횟수와 이떄의 테스트셋 오차 값을 이용해 파일 이름을 만들어 hdf5라는 확장자로 저장한다. 
# ex> 100번째 에포크를 실행한 후 결과 오차가 0.0612라면 파일명은 100-1.0612가 되는 것

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint # 모델을 저장하기위해 콜백함수 호출

import pandas as pd
import numpy
import os
import tensorflow as tf

# seed 값 설정
numpy.random.seed(3)
tf.random.set_seed(3)

df_pre = pd.read_csv('../dataset/wine.csv', header=None)
df = df_pre.sample(frac=1)

dataset = df.values
X = dataset[:,0:12]
Y = dataset[:,12]

# 모델의 설정
model = Sequential()
model.add(Dense(30,  input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(loss='binary_crossentropy',
          optimizer='adam',
          metrics=['accuracy'])

# 모델 저장 폴더 설정
MODEL_DIR = './model/' # 모델을 저장하는 폴더
if not os.path.exists(MODEL_DIR): # 만일 위의 폴더가 존재하지 않으면
   os.mkdir(MODEL_DIR) # 이 이름의 폴더를 만들어줌

# 모델 저장 조건 설정
modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5" #모델이 저장될 곳 지정
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)
# 값을 1로 정하면 해당 함수의  진행사항이 출력, 0이면 출력 안됨, #함수에 모델이 앞서 저장한 모델보다 나아졌을때만 저장하려면 세이브 베스트를 트루로

# 모델 실행 및 저장
model.fit(X, Y, validation_split=0.2, epochs=200, batch_size=200, verbose=0, callbacks=[checkpointer])
# 모델을 학슴할 ㄸ ㅐ마다 위에서 정한 checkpoint의 값을 받아 지정된 곳에 모델을 저장 

#  그래프로 표현해보자.. 끝이없네 
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint

import pandas as pd
import numpy
import os
import matplotlib.pyplot as plt
import tensorflow as tf

# seed 값 설정
numpy.random.seed(3)
tf.random.set_seed(3)

df_pre = pd.read_csv('../dataset/wine.csv', header=None)
df = df_pre.sample(frac=0.15) # 데이터의 15퍼만 가져옴

dataset = df.values
X = dataset[:,0:12]
Y = dataset[:,12]

# 모델의 설정
model = Sequential()
model.add(Dense(30,  input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 모델 컴파일
model.compile(loss='binary_crossentropy',
          optimizer='adam',
          metrics=['accuracy'])

# 모델 저장 폴더 설정
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
   os.mkdir(MODEL_DIR)

# 모델 저장 조건 설정
modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)

# 모델 실행 및 저장
history = model.fit(X, Y, validation_split=0.33, epochs=3500, batch_size=500) # 테스트셋 33퍼

# y_vloss에 테스트셋으로 실험 결과의 오차 값을 저장
y_vloss=history.history['val_loss']

# y_acc 에 학습 셋으로 측정한 정확도의 값을 저장
y_acc=history.history['accuracy']

# x값을 지정하고 정확도를 파란색으로, 오차를 빨간색으로 표시
x_len = numpy.arange(len(y_acc))
plt.plot(x_len, y_vloss, "o", c="red", markersize=3)
plt.plot(x_len, y_acc, "o", c="blue", markersize=3)

plt.show()

# 학습의 자동중단 : 학습이 진행될수록 학습셋의 정확도는 올라가지만, 과적합 때문에 테스트셋의 결과는 점점 나빠지게 된다.
# 케라스에는 학습이 진행되어도 테스트셋 오차가 줄어들지 않으면 학습을 멈추게 하는 함수가 있다. 바로 EarlyStopping() 이다.
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint,EarlyStopping

import pandas as pd
import numpy
import os
import tensorflow as tf

# seed 값 설정
numpy.random.seed(3)
tf.random.set_seed(3)

df_pre = pd.read_csv('../dataset/wine.csv', header=None)
df = df_pre.sample(frac=0.15)

dataset = df.values
X = dataset[:,0:12]
Y = dataset[:,12]

model = Sequential()
model.add(Dense(30,  input_dim=12, activation='relu'))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
          optimizer='adam',
          metrics=['accuracy'])

# 모델 저장 폴더 만들기
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
   os.mkdir(MODEL_DIR)

modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"

# 모델 업데이트 및 저장
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)

# 학습 자동 중단 설정
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=100)

model.fit(X, Y, validation_split=0.2, epochs=3500, batch_size=500, verbose=0, callbacks=[early_stopping_callback,checkpointer])

#전체 샘플의 15퍼센트만 사용했으므로 780개의 샘플이 입력되었다. 전체반복값을 3500으로 했으나, 마지막 업데이트 경우 682였다
# 이후 100번가량 모델이 나아지지 않자 학습이 자동 중단되었다 

# 선형 회귀 적용하기
# 집값의 가장 큰 요인은 깨끗한 공기일까 ? 주어진 환경과 집값의 변동을 학습해서 환경 요인만 놓고 집값을 예측해보자
# 선형 회귀는 마지막에 참과 거짓을 구분할 필요가 없다. 출력층에 활성화 함수를 지정할 필요도 없다.
# 또 모델의 학습이 어느 정도 되었는지 확인하기 위해 예측 값과 실제 값을 비교하는 부분을 추가해보자

#-*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

import numpy
import pandas as pd
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

df = pd.read_csv("../dataset/housing.csv", delim_whitespace=True, header=None)
'''
print(df.info())
print(df.head())
'''
dataset = df.values
X = dataset[:,0:13]
Y = dataset[:,13]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

model = Sequential()
model.add(Dense(30, input_dim=13, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error',
              optimizer='adam')

model.fit(X_train, Y_train, epochs=200, batch_size=10)

# 예측 값과 실제 값의 비교
Y_prediction = model.predict(X_test).flatten() #flatten 함수는 데이터를 모두 1차원으로 바꿔 읽기 쉽게 해 주는 함수
for i in range(10):
    label = Y_test[i]
    prediction = Y_prediction[i]
    print("실제가격: {:.3f}, 예상가격: {:.3f}".format(label, prediction))


#cnn익히기. 지금까지 배운 딥런이을 이용해 손글씨 이미지를 예측해 보자 

# 1. 데이터 전처리 MNIST 데이터를 불러온다
from keras.datasets import mnist # 이떄 불러온 데이터를 X로, 이 이미지에 0~9까지 붙인 이름표를 Y_class로 구분하여 명명한다
# 또 학습에 사용될 부분은 train으로 테스트에 사용 될 부분은 test라는 이름으로 불러오겠다.


(X_train, Y_class_train), (X_test,Y_class_test) = mnist.load_data()

# 케라스의 데이터 이미지 70000개중 60000를 학습용으로, 10000으로 테스트용으로 구분해 놓고 있다 이를 확인해보자

print("학습 셋 이미지 수: %d 개 " % (X_train.shape[0])) # shape[0] 은 행 갯수 반환 1은 열갯수이다
print("테스트 셋 이미지 수 : %d개" % (X_test.shape[0]))

# 불러온 이미지중  한개만 다시 불러와본다 imshow() 함수를 통해 이미지를 출력하고, X_train[0] 을 통해 첫번째 이미지  출력
import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap='Greys')
plt.show()

# 이 이미지를 컴퓨터는 어찌 인식할까 ?  28 *25 = 784개의 픽셀로 이루어져 있다. 각 픽셀은 밝기 정도에따라 0에서 255까지 등급을 매긴다
# 흰색이 0이라면 글씨가 들어간 곳은 1` - 255까지 숫자중 하나로 채워져 긴 행렬로 이루어진 하나의 집합으로 변환된다. 다음코드로 확인해보자
import sys
for x in X_train[0]:
    for i in x:
        sys.stdout.write('%d\t' % i)
    sys.stdout.write('\n')
# 이렇게 이미지는 다시 숫자의 집합으로 바뀌어 학습셋으로 사용된다. 앞서  진행한 예제들과 마찬가지로 속성을 담은 데이터를 딥러닝에 집어넣고
# 클래스를 예측하는 문제로 전환시키는것이다 784개의 속성을 이용해 10개의 클래스중 하나를 맞히는 문제가 됨 
# 이제 주워진 2차워 배열을 1차원 배열로 바꿔주느다. reshape() 함수를 사용 reshape(총 샘플수,1차원속성의 수 형식으로 지정)
# 케라스는 데이터를 0에서 1 사이의 값으로 변환한 다음 구동할 때 최적의 성능을 보인다 따라서 0-255를 0-1로 바꾸어 줘야함
# 이렇게 데이터 폭이 클 때 적절한 값으로 바꾸어 주는 과정을 데이터 정규화 라고 한다 astype() 함수로 실수로 바꾸어 준 뒤 255로 나눈다

X_train = X_train.astype('flot64')
x_train = X_train / 255

# 이제 숫자 이미지에 매겨진 이름을 확인해본다  실제로 이 숫자의 레이블이 어떤지를 불러오고자 Y_class_train[0]을 다음과 같이 출력해본다.
print("class : %d " % (Y_class_train[0]))
# 이후 원 핫 인코딩을 거쳐 실행해본다
#-*- coding: utf-8 -*-

from keras.datasets import mnist
from keras.utils import np_utils

import numpy
import sys
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# MNIST데이터셋 불러오기
(X_train, Y_class_train), (X_test, Y_class_test) = mnist.load_data()

print("학습셋 이미지 수 : %d 개" % (X_train.shape[0]))
print("테스트셋 이미지 수 : %d 개" % (X_test.shape[0]))

# 그래프로 확인
import matplotlib.pyplot as plt
plt.imshow(X_train[0], cmap='Greys')
plt.show()

# 코드로 확인
for x in X_train[0]:
    for i in x:
        sys.stdout.write('%d\t' % i)
    sys.stdout.write('\n')

# 차원 변환 과정
X_train = X_train.reshape(X_train.shape[0], 784)
X_train = X_train.astype('float64')
X_train = X_train / 255

X_test = X_test.reshape(X_test.shape[0], 784).astype('float64') / 255

#print(X_train[0])

# 클래스 값 확인
print("class : %d " % (Y_class_train[0]))

# 바이너리화 과정
Y_train = np_utils.to_categorical(Y_class_train, 10) # 클래스 ,클래스의 수 원 핫 인코딩
Y_test = np_utils.to_categorical(Y_class_test, 10)

print(Y_train[0])


# 딥러닝 기본 프레임 만들기

#-*- coding: utf-8 -*-

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint,EarlyStopping

import matplotlib.pyplot as plt
import numpy
import os
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# MNIST 데이터 불러오기
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 784).astype('float32') / 255
X_test = X_test.reshape(X_test.shape[0], 784).astype('float32') / 255

Y_train = np_utils.to_categorical(Y_train, 10)
Y_test = np_utils.to_categorical(Y_test, 10)

# 모델 프레임 설정
model = Sequential()
model.add(Dense(512, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))

# 모델 실행 환경 설정
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 모델 최적화 설정
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10)

# 모델의 실행
history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=30, batch_size=200, verbose=0, callbacks=[early_stopping_callback,checkpointer])

# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))

# 테스트 셋의 오차
y_vloss = history.history['val_loss']

# 학습셋의 오차
y_loss = history.history['loss'] # 학습셋의 오차는 1에서 학습셋의 정확도를 뺀 것

# 그래프로 표현
x_len = numpy.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c="red", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right')
# plt.axis([0, 20, 0, 0.35])
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# 컨볼루션 신경망 : 입력된 이미지에 다시 한번 특징을 추출하기 위해서 커널(슬라이딩윈도)을 도입하는 기법이다
# 2*2 커널을  한칸 씩 옮기며 적용시켜서 새로운 층을 만든다. 이렇게 만들면 더욱 정교한 특징을 추출 할 수 있다.
# 케라스에서 컨볼루션 층을 추가하는 함수는 Conv2D() 이다. 다음과 같이 컨볼루션 층을 적용하여 손글씨 인식률을 높인다
# mode.add(Conv2D(32,kenel_size=(3,3),input_shape(28,28,1),activation='relu'))
# 첫번쨰 인자 : 커널 몇개적용할거임? 여기선 32
# 두번째 인자 : 커널 크기 적용 행,열 형식이다
# 세번째 인자 : 맨 처음 층에 입력되는 값

# 맥스 풀링 : 컨볼루션한 이미지가 여전히 클 경우 다시한번 축소한다 최댓값만을 뽑아내는 맥스풀링 평균값을 뽑아내는 평균풀링 등이 있다.
# 구역을 나눈 뒤 구역에서 가장 큰 값 추출한다 이 과정을 거쳐 불필요한 값 간추린다
# model.add(MaxPooling2D(pool_size=2)) # 풀 사이즈는 창의 크기를 결정하는것으로 2로 정하면 전체 크기가 반으로 줄어든다


# 드롭아웃, 플래튼
# 드롭아웃 : 은닉층에 배치된 노드 중 일부를 임의로 꺼준다. 랜덤하게 노드를 꺼 학습데이터에 치우치는것을 막을 수 있따.
# mode.add(Dropout(0.25)) 25퍼의 노드를 끄는것이다 그 후 플래튼함수로 1차원으로 바꿔줌


from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.callbacks import ModelCheckpoint,EarlyStopping

import matplotlib.pyplot as plt
import numpy
import os
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# 데이터 불러오기

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32') / 255
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32') / 255
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

# 컨볼루션 신경망의 설정
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(28, 28, 1), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,  activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 모델 최적화 설정
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)

modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10)

# 모델의 실행
history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=30, batch_size=200, verbose=0, callbacks=[early_stopping_callback,checkpointer])

# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))

# 테스트 셋의 오차
y_vloss = history.history['val_loss']

# 학습셋의 오차
y_loss = history.history['loss']

# 그래프로 표현
x_len = numpy.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c="red", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# 딥러닝을 이용한 자연어 처리 : 대화형 인공지능이러고 불리는 ai비서들이 서로 경쟁하고 있다.
# 이것의 필수 능력은 사람의 언어를 이해하는 것 이다. 듣고 무엇을 의미하는지 알아야 서비스를 제공해 줄 수 있으니까
# 이러한 능력을 만들어 주는 자연어 처리의 기본을 배워보자
# 1. 텍스트의 토큰화 : 텍스트를 잘게 나눈다. 잘게 나뉜 하나의 단위를 토큰 이라 한다

from tensorflow.keras.preprocessing.text import text_to_word_sequence
text = "해보지 않으면 해낼 수 없다"
result = text_to_word_sequence(text)
print(result)

from tensorflow.keras.preprocessing.text import Tokenizer # 단어의 빈도 수를 쉽게 계산 할 수 있다.
docs = ['먼저 텍스트의 각 단어를 나누어 토큰화 합니다', '텍스트의 단어로 토큰화해야 딥런이에서 인식됩니다', '토큰화한 결과는 딥러닝에서 사용할 수 있습니다']
token = Tokenizer() # 토큰화 함수 지정 
token.fit_on_texts(docs) # 토큰화 함수에 문자 적용
print(token.word_counts)

#document_count 함수를 이용하면 총 몇개의 문장이 들어있는지도 셀 수 있다
print(token.document_count)

# 또한 word_docs() 함수를 통해 각 단어들이 몇개 의 문장에 나오는가를 세어서 출력할 수 있다. 출력되는 순서는 랜덤
print(token.word_docs)

# 각 단어에서 매겨진 인덱스 값을 출력하려면 word_index() 함수를 사용하면 됩니다
print(token.word_index)

from tensorflow.keras.preprocessing.text import Tokenizer
text = "오랫동안 꿈꾸는 이는 그 꿈을 닮아간다"

token = Tokenizer()
token.fit_on_texts([text])
print(token.word_index)

# 이제 각 단어를 원-핫 인코딩 방식으로 표현해보겠습니다. 케라스에서 제공하는 Tokenizer의 text_to_sequence() 함수를 사용해서 앞서 만들어진 토큰의 인덱스로만 채워진 새로운 배열을 만들어준다
x = token.texts_to_sequences([text])
print(x)

# 이제 1`-6까지의 정수로 인덱스에 되어 있는 것을 0과 1로만 이루어진 배열로 바꾸어 주는 to_categorical()로 인코딩 과정을 진행합니다

from keras.utils import to_categorical

# 인덱수 수에 하나를 추가해서 원-핫 인코딩 배열 만들기
word_size = len(token.word_index) +1 
x = to_categorical(x,num_classes=word_size)

print(x)

# 단어 임베딩
# 원-핫 인코딩을 그대로 사용하면 벡터의 길이가 너무 길어진다는 단점이 있습니다. 예를들어 만개의 단어 토큰으로 이루어지는 말뭉치를 다룬다고 할떄, 원-핫 인코딩으로 벡터화하면 9,999개의 0과 1한1 하나로 이루어진 단어벡터를 만개 만들어야한다
# 이 낭비를 해결하기 위해 등장한 것이 단어 임베딩이다
# 단어 임베딩은 각 단어간의 유사도를 계산했기 떄문에 가능하다 그렇다면 이 유사도는 어떻게 구할까 ? 앞서 등장한 오차 역전파가 다시 등장한다

from keras.layers import Embedding
model = Sequential()
medel.add(Embedding(16,4)) 
# 임베딩 함수는 최소 2개의 매개변수를 필요로 하는데, 바로 입력과 출력의 크기이다 16은 입력될 총 단어의 수 4는 출력될 벡터의 크기이다
Embedding(16,4 input_length=2) 라고 하면 총 입력되는 단어의 수는 16개이지만 매번 2개씩만 넣겠다는것


# 원-핫 인코딩
# 우리는 문장을 컴퓨터가 알아들을 수 있게 토큰화하고 단어의 빈도수를 확인했다 하지만 단순한 출현 빈도만 가지고는 해당 단어가 문장 어디서 왔는지, 각 단어의 순서는 어떠했는지 등에 관한 정보를 얻을 수 없다.
# 단어가 문장의 다른 요소와 어떤 관계를 가지고 있는지 알아보는 방법이 필요하다. 기본적인 방법으로는 원-핫 인코딩이 있다.
# 각 단어를 모두 0으로 주고 우너하는 단어만 1로 바꾸어 줌 파이썬 배열의 인덱스는 0부터 시작하브로 맨 앞에 0 추가된다

# -*- coding: utf-8 -*-
# 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

import numpy
import tensorflow as tf
from numpy import array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten,Embedding


#주어진 문장을 '단어'로 토큰화 하기

#케라스의 텍스트 전처리와 관련한 함수중 text_to_word_sequence 함수를 불러 옵니다.
from tensorflow.keras.preprocessing.text import text_to_word_sequence
 
# 전처리할 텍스트를 정합니다.
text = '해보지 않으면 해낼 수 없다'
 
# 해당 텍스트를 토큰화 합니다.
result = text_to_word_sequence(text)
print("\n원문:\n", text)
print("\n토큰화:\n", result)
 
#단어 빈도수 세기

#전처리 하려는 세개의 문장을 정합니다.
 
docs = ['먼저 텍스트의 각 단어를 나누어 토큰화 합니다.',
       '텍스트의 단어로 토큰화 해야 딥러닝에서 인식됩니다.',
       '토큰화 한 결과는 딥러닝에서 사용 할 수 있습니다.',
       ]
 
# 토큰화 함수를 이용해 전처리 하는 과정입니다.
token = Tokenizer()             # 토큰화 함수 지정
token.fit_on_texts(docs)       # 토큰화 함수에 문장 적용
 
#단어의 빈도수를 계산한 결과를 각 옵션에 맞추어 출력합니다. 
 
print("\n단어 카운트:\n", token.word_counts) 
#Tokenizer()의 word_counts 함수는 순서를 기억하는 OrderedDict클래스를 사용합니다.
 
#출력되는 순서는 랜덤입니다. 
print("\n문장 카운트: ", token.document_count)
print("\n각 단어가 몇개의 문장에 포함되어 있는가:\n", token.word_docs)
print("\n각 단어에 매겨진 인덱스 값:\n",  token.word_index)


# 텍스트 리뷰 자료를 지정합니다.
docs = ["너무 재밌네요","최고예요","참 잘 만든 영화예요","추천하고 싶은 영화입니다","한번 더 보고싶네요","글쎄요","별로예요","생각보다 지루하네요","연기가 어색해요","재미없어요"]

# 긍정 리뷰는 1, 부정 리뷰는 0으로 클래스를 지정합니다.
classes = array([1,1,1,1,1,0,0,0,0,0])

# 토큰화 
token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)
x = token.texts_to_sequences(docs)
print("\n리뷰 텍스트, 토큰화 결과:\n",  x)

# 패딩, 서로 다른 길이의 데이터를 4로 맞추어 줍니다.
padded_x = pad_sequences(x, 4)  
print("\n패딩 결과:\n", padded_x)
 
#딥러닝 모델
print("\n딥러닝 모델 시작:")

#임베딩에 입력될 단어의 수를 지정합니다.
word_size = len(token.word_index) +1
 
#단어 임베딩을 포함하여 딥러닝 모델을 만들고 결과를 출력합니다.
model = Sequential()
model.add(Embedding(word_size, 8, input_length=4)) #워드사이즈는 몇개를 출력할것인지
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(padded_x, classes, epochs=20)
print("\n Accuracy: %.4f" % (model.evaluate(padded_x, classes)[1]))

# 순환 신경망 : 여러 개의 데이터가 입력되었을 때 , 앞에 데이터를 잠시 기억한다, 그 이후 기억된 데이터가 얼마나 중요한지 판단하여 별도의 가중치를 준 다음 다음 데이터로 넘어간다
# LSTN : 입력과 순환시, 즉 반복되기 직전에 다음 층으로 기억된 값을 넘길지 안넘길지를 관리하는 단계가 하나 더 추가됨

# 입력된 문장의 의미를 파악하는 것은 곧 모든 단어를 종합하여 하나의 카테고리로 분류하는 작업이라고 할 수 있다. 예를 들어 '안녕 날씨가 참 좋네' 라는 말은 인사 카테고리에 분류 해야한다
import numpy
from keras.datasets import reuters

# 불러온 데이터를 학습셋과 데이터셋으로 나눈다
(X_train, Y_train), (x_text,Y_text) = reuters.load_data(num_words=1000, test_split=0.2)

# 데이터 확인 후 출력
category = numpy.max(Y_train) +1 # Y_train의 종류를 구한다
print(X_train[0])
# 출력을 해보니 단어가 나오는게 아니라 숫자가 나온다. 딥러닝은 단어를 그대로 사용하지 못하고 숫자로 변환한다음 학습 할 수 있다. 3이라는건 3번째로 많이 언급된 단어라는 것
# 케라스는 이미 tokenizer()를 마친 데이터이다
# 기사 안에 단어중엔 사용빈도가 작은것들이 있다. 이런건 제외하고 빈도가 높은 단어만 불러오자 이때 사용하는것이 word=1000 이다 빈도가 1~1000에 해당하는 단어만 선택해서 불러온다
# 또 하나 주의해야 할 점은 각 기사의 단어의 수가 제각각 다르므로 이를 동일하게 맞춰줘야 한다. Sequence() 를 이용하자
from.keras.preprocessing import Sequence

#데이터 전처리
X_train = sequence.pad_sequence(X_train, maxlen=100)
X_test = sequence.pad_sequence(X_text, maxlen=100) # 단어수를 100개로 맞추라는 것  이다. 100에 모자랄때는 0으로 채운다

# 이제 y데이터에 원-핫 인코딩 처리하여 전처리를 마친다
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)


# -*- coding: utf-8 -*-
# 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

import numpy
import tensorflow as tf
import matplotlib.pyplot as plt

# 로이터 뉴스 데이터셋 불러오기
from keras.datasets import reuters
from keras.models import Sequential
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense,LSTM,Embedding
from keras.layers import Dense, LSTM, Embedding
from keras.preprocessing import sequence
from keras.utils import np_utils



# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# 불러온 데이터를 학습셋, 테스트셋으로 나누기
(X_train, Y_train), (X_test, Y_test) = reuters.load_data(num_words=1000, test_split=0.2)

# 데이터 확인하기
category = numpy.max(Y_train) + 1
print(category, '카테고리')
print(len(X_train), '학습용 뉴스 기사')
print(len(X_test), '테스트용 뉴스 기사')
print(X_train[0])

# 데이터 전처리
x_train = sequence.pad_sequences(X_train, maxlen=100)
x_test = sequence.pad_sequences(X_test, maxlen=100)
y_train = np_utils.to_categorical(Y_train)
y_test = np_utils.to_categorical(Y_test)

# 모델의 설정
model = Sequential()
model.add(Embedding(1000, 100))
model.add(LSTM(100, activation='tanh'))
model.add(Dense(46, activation='softmax'))

# 모델의 컴파일
model.compile(loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

# 모델의 실행
history = model.fit(x_train, y_train, batch_size=100, epochs=20, validation_data=(x_test, y_test))

# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(x_test, y_test)[1]))


# 테스트 셋의 오차
y_vloss = history.history['val_loss']

# 학습셋의 오차
y_loss = history.history['loss']

# 그래프로 표현
x_len = numpy.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c="red", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# LSTM과 CNN의 조합을 이용한 영화 리뷰 분류하기

# -*- coding: utf-8 -*-
# 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Conv1D, MaxPooling1D
from keras.datasets import imdb

import numpy
import tensorflow as tf
import matplotlib.pyplot as plt

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.random.set_seed(3)

# 학습셋, 테스트셋 지정하기
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=5000)

# 데이터 전처리
x_train = sequence.pad_sequences(x_train, maxlen=100)
x_test = sequence.pad_sequences(x_test, maxlen=100)

# 모델의 설정 이부분 잘 이해 안됨 공부 필요
model = Sequential()
model.add(Embedding(5000, 100))
model.add(Dropout(0.5))
model.add(Conv1D(64, 5, padding='valid', activation='relu',strides=1))
model.add(MaxPooling1D(pool_size=4))
model.add(LSTM(55))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.summary()

# 모델의 컴파일
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 모델의 실행
history = model.fit(x_train, y_train, batch_size=100, epochs=5, validation_data=(x_test, y_test))

# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(x_test, y_test)[1]))


# 테스트 셋의 오차
y_vloss = history.history['val_loss']

# 학습셋의 오차
y_loss = history.history['loss']

# 그래프로 표현
x_len = numpy.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c="red", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# 생산적 적대 신경망 (gan): 딥러닝 원리를 이용해 가상의 이미지를 생성하는 알고리즘이다. 예를 들어 얼굴을 만든다면, 이미지 픽셀들이 어떻게 조합되어야 우리가 생각하는 '얼굴'의 형상이 되는지를 딥러닝 알고리즘이 예측한 결과이다
# 진짜같은 가짜를 만들기 위해 GAN알고리즘 내부에서는 적대적인 경합을 진행한다
# 예를들어 정교하게 위조지폐를 만들기 위해 노력하는 범인 그걸 검거하기 위해 애쓰는 경찰 , 한쪽은 가짜를 만들고 한쪽은 진짜와 비교하는 경합의 과정을 이용한 것이다
# 가짜를 만들어 내는 파트를 '생성자' 진위를 가려내는것을 '판별자'라고 한다

# 가짜 제조공장, 생성자 : 가상 이미지를 만들어 내는 공간이다. 처음엔 랜덤한 픽셀 값으로 채워진 가짜 이미지로 시작해서, 판별자의 판별 결과에 따라 지속적으로 업데이트 하며 점차 원하는 이미지를 만들어 갑니다
# 기존 컨볼루션과 차이점은 최적화나 컴파일 과정이 없다, 풀링도 없고 패딩과정은 포함. 패딩과정을 하는 이유는 진짜 이미지와 같은 크기여야 하기 떄문이다 padding='same'을 통해 쉽게 처리 가능하다
# 또 필요한것이 배치 정규화 . 배치 정규화란 입력 데이터 평균이 0 , 분산이 1이 되도록 배치한느것, 이를통해 다음층으로 입력될 값을 일정하게 재배치 하는 역할을 한다 이를 쉽게 적용하게끔  Batchnomalization() 함수 이용
# 또한 생성자의 활성화 함수로는 relu() 를 쓰고 넘겨주기 직전엔 tanh() 함수를 쓰고 있다 이 함수를 쓰면 값을 -1~1 사이로 맞출 수 있다.

# 진위를 가려내는 장치, 판별자 : 이제 생성자에서 넘어온 이미지가 가짜인지 진짜인지 구별하는 판별자를 만들어 보자 판별자는 컨볼루션 신경망을 그대로 가져와서 만들면 된다 binary_crossentropy() 와 최적화 함수 adam()을 사용하면 된다
# 판별자는 진위를 가려줄 뿐 자기 자신이 학습을 해서는 안된다. 판별자가 얻은 가중치는 생성자에게 넘거주어 업데이트 된 이미지를 만들게 한다 따라서 가중치 저장 학습 코드 없다

# 이제 생성자와 판별자를 연결시키고, 학습을 진행하며 기타 옵션들을 설정한다. 연결시킨다는것은 생성자에서 나온 출력을 판별자에게 넣어 진위 여부판별 정확도가 0.5에 가까워 질때 학습은 종료 생성자(G()) 판별자 (D()) 데이터값(x)
#-*- coding: utf-8 -*-

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense, Reshape, Flatten, Dropout
from tensorflow.keras.layers import BatchNormalization, Activation, LeakyReLU, UpSampling2D, Conv2D
from tensorflow.keras.models import Sequential, Model

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

#이미지가 저장될 폴더가 없다면 만듭니다.
import os
if not os.path.exists("./gan_images"):
    os.makedirs("./gan_images")

np.random.seed(3)
tf.random.set_seed(3)

#생성자 모델을 만듭니다.
generator = Sequential()
generator.add(Dense(128*7*7, input_dim=100, activation=LeakyReLU(0.2))) #128은 임의으 노드 수, 100차원 크기의 랜덤 백터, 7*7은 이미지의 최초 크기
generator.add(BatchNormalization())
generator.add(Reshape((7, 7, 128))) # 컨볼루션 레이어가 받아드릴 수 있는 형태로 정해준다
generator.add(UpSampling2D()) # 이미지 크기 두배로
generator.add(Conv2D(64, kernel_size=5, padding='same')) #커널 64개 추가, 3*3크기 커널, 모자라는부분 0으로 채움
generator.add(BatchNormalization()) #재배치함
generator.add(Activation(LeakyReLU(0.2))) #relu함수를 쓰면 불안정한 경우 많아 이거씀
generator.add(UpSampling2D()) # 이미지 크기 두배로
generator.add(Conv2D(1, kernel_size=5, padding='same', activation='tanh'))

#판별자 모델을 만듭니다.
discriminator = Sequential()
discriminator.add(Conv2D(64, kernel_size=5, strides=2, input_shape=(28,28,1), padding="same")) #커널 윈도를 2칸씩 움직인다 가로 세로 크기가 더 줄어들어 새로운 특징을 뽑아주는 효과가 있다
discriminator.add(Activation(LeakyReLU(0.2)))
discriminator.add(Dropout(0.3))
discriminator.add(Conv2D(128, kernel_size=5, strides=2, padding="same"))
discriminator.add(Activation(LeakyReLU(0.2)))
discriminator.add(Dropout(0.3))
discriminator.add(Flatten())
discriminator.add(Dense(1, activation='sigmoid'))
discriminator.compile(loss='binary_crossentropy', optimizer='adam')
discriminator.trainable = False # 학습 기능을 꺼준다

#생성자와 판별자 모델을 연결시키는 gan 모델을 만듭니다.
ginput = Input(shape=(100,)) # 랜덤한 100개의 벡터를 케라스의 인풋에 집어넣어 생성자에 입력할 ginput 만드는 과정
dis_output = discriminator(generator(ginput)) # 생성자 모델에 g input입력  그결과 입력값이 판별자 모델이 들어감 참,거짓 결과를 판단하는 변수이다
gan = Model(ginput, dis_output)
gan.compile(loss='binary_crossentropy', optimizer='adam') # 참과 거짓을 판단하는 이진로스 함수와 최적화 함수를 통해 컴파일 한다
gan.summary()

#신경망을 실행시키는 함수를 만듭니다.
def gan_train(epoch, batch_size, saving_interval): # 학습이 진행되도록 한다

  # MNIST 데이터 불러오기

  (X_train, _), (_, _) = mnist.load_data()  # 앞서 불러온 적 있는 MNIST를 다시 이용합니다. 단, 테스트과정은 필요없고 이미지만 사용할 것이기 때문에 X_train만 불러왔습니다.
  X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
  X_train = (X_train - 127.5) / 127.5  # 픽셀값은 0에서 255사이의 값입니다. 이전에 255로 나누어 줄때는 이를 0~1사이의 값으로 바꾸었던 것인데, 여기서는 127.5를 빼준 뒤 127.5로 나누어 줌으로 인해 -1에서 1사이의 값으로 바뀌게 됩니다.
  #X_train.shape, Y_train.shape, X_test.shape, Y_test.shape

  true = np.ones((batch_size, 1)) # 한 번에 몇 개의 실제 이미지와 몇 개의 가상 이미지를 판별자에 넣을지 결정하는 변수이다. 모두 실제 이미지를 입력했으므로 참(1) 이라는 레이블 붙인다 모두 참이라는 레이블을 가진 변수 만듬
  fake = np.zeros((batch_size, 1))

  for i in range(epoch):
          # 실제 데이터를 판별자에 입력하는 부분입니다.
          idx = np.random.randint(0, X_train.shape[0], batch_size) #랜덤으로 이미지를 불러 , batch_size만큼 가져온다
          imgs = X_train[idx] #선택된 이미지를 가져온다
          d_loss_real = discriminator.train_on_batch(imgs, true) #판별을 시작한다

          #가상 이미지를 판별자에 입력하는 부분입니다.
          noise = np.random.normal(0, 1, (batch_size, 100)) #생성자에게 집어넣을 가상 이미지를 만드는 부분 0-1 사이로 batch_size만큼 100개뽑아
          gen_imgs = generator.predict(noise)
          d_loss_fake = discriminator.train_on_batch(gen_imgs, fake)
http://localhost:8888/notebooks/Desktop/deeplearning/run_project/20_GAN.ipynb#
          #판별자와 생성자의 오차를 계산합니다.
          d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
          g_loss = gan.train_on_batch(noise, true)

          print('epoch:%d' % i, ' d_loss:%.4f' % d_loss, ' g_loss:%.4f' % g_loss)

        # 이부분은 중간 과정을 이미지로 저장해 주는 부분입니다. 본 장의 주요 내용과 관련이 없어
        # 소스코드만 첨부합니다. 만들어진 이미지들은 gan_images 폴더에 저장됩니다.
          if i % saving_interval == 0:
              #r, c = 5, 5
              noise = np.random.normal(0, 1, (25, 100))
              gen_imgs = generator.predict(noise)

              # Rescale images 0 - 1
              gen_imgs = 0.5 * gen_imgs + 0.5

              fig, axs = plt.subplots(5, 5)
              count = 0
              for j in range(5):
                  for k in range(5):
                      axs[j, k].imshow(gen_imgs[count, :, :, 0], cmap='gray')
                      axs[j, k].axis('off')
                      count += 1
              fig.savefig("gan_images/gan_mnist_%d.png" % i)

gan_train(4001, 32, 200)  #4000번 반복되고(+1을 해 주는 것에 주의), 배치 사이즈는 32,  200번 마다 결과가 저장되게 하였습니다.


# 이미지의 특징을 추출하는 오토 인코더 : gan은 세상에 존재하지 않는 이미지를 만드는 것이라면, 오토인코더는 사람의 특징을 유추할 수 있는 것들이 모여 이미지가 만들어 진다
# 입력과 똑같은 크기의 출력층을 만들고, 입력층보다 적은 수의 노드를 가진 은닉층을 중간에 넣어 줌으로써 차원을 줄여준다. 이떄, 소실된 데이터를 복원하기 위해 학습을 시작하고, 이과정을 통해 입력 데이터의 특징을 효율적으로 응축한 새로운 출력이 나오는 원리

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Flatten, Reshape
import matplotlib.pyplot as plt
import numpy as np

#MNIST데이터 셋을 불러옵니다.

(X_train, _), (X_test, _) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32') / 255
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32') / 255

#생성자 모델을 만듭니다.
autoencoder = Sequential()

# 인코딩 부분입니다. 입력된 차원을 축소시킨다 줄이는 방법으로 맥스풀링
autoencoder.add(Conv2D(16, kernel_size=3, padding='same', input_shape=(28,28,1), activation='relu')) #패딩옵션없기에 풀링과 언샘플링의수가 다르다 ?? 어렵다 
autoencoder.add(MaxPooling2D(pool_size=2, padding='same'))
autoencoder.add(Conv2D(8, kernel_size=3, activation='relu', padding='same'))
autoencoder.add(MaxPooling2D(pool_size=2, padding='same'))
autoencoder.add(Conv2D(8, kernel_size=3, strides=2, padding='same', activation='relu'))

# 디코딩 부분이 이어집니다. 차원을 다시 점차 늘려 입력 값과 똑같은 값 내보낸다 늘이는 방법으로 언샘플링
autoencoder.add(Conv2D(8, kernel_size=3, padding='same', activation='relu')) 
autoencoder.add(UpSampling2D())
autoencoder.add(Conv2D(8, kernel_size=3, padding='same', activation='relu'))
autoencoder.add(UpSampling2D())
autoencoder.add(Conv2D(16, kernel_size=3, activation='relu'))
autoencoder.add(UpSampling2D())
autoencoder.add(Conv2D(1, kernel_size=3, padding='same', activation='sigmoid'))

# 전체 구조를 확인해 봅니다.
autoencoder.summary()

# 컴파일 및 학습을 하는 부분입니다.
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.fit(X_train, X_train, epochs=50, batch_size=128, validation_data=(X_test, X_test))

#학습된 결과를 출력하는 부분입니다.
random_test = np.random.randint(X_test.shape[0], size=5)  #테스트할 이미지를 랜덤하게 불러옵니다.
ae_imgs = autoencoder.predict(X_test)  #앞서 만든 오토인코더 모델에 집어 넣습니다.

plt.figure(figsize=(7, 2))  #출력될 이미지의 크기를 정합니다.

for i, image_idx in enumerate(random_test):    #랜덤하게 뽑은 이미지를 차례로 나열합니다.
   ax = plt.subplot(2, 7, i + 1) 
   plt.imshow(X_test[image_idx].reshape(28, 28))  #테스트할 이미지를 먼저 그대로 보여줍니다.
   ax.axis('off')
   ax = plt.subplot(2, 7, 7 + i +1)
   plt.imshow(ae_imgs[image_idx].reshape(28, 28))  #오토인코딩 결과를 다음열에 출력합니다.
   ax.axis('off')
plt.show()

# 전이 학습을 통해 딥러닝의 성능 극대화 하기 : 딥러닝의 데이터 양이 충분하지 않을때 활용할 수 있는 방법들, 딥러닝은 스르로 중요한 속성을 뽑아 쓰기 때문에 비교적 많은 양의 데이터가 필요하다
# 여러 방법중 수만장에 달하는 기존 이미지를 학습한 정보에서 가져와 내 프로젝트에 활용하는것을 전이학습 이라 한다. 방대한 자료를 통해 미리 학습한 가중치 값을 가져와 내 프로젝트에 활용하는 방법

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout, Flatten, Dense, Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers, initializers, regularizers, metrics

np.random.seed(3)
tf.random.set_seed(3)

train_datagen = ImageDataGenerator(rescale=1./255,   # 데이터 수를 늘리는 함수, rescale 은 주어진 이미지 크기를 바꿔줌
                                  horizontal_flip=True,     #수평 대칭 이미지를 50% 확률로 만들어 추가합니다.
                                  width_shift_range=0.1,  #전체 크기의 10% 범위에서 좌우로 이동합니다.
                                  height_shift_range=0.1, #마찬가지로 위, 아래로 이동합니다.
                                  #rotation_range=5,      # 정해진 각도만큼 회전
                                  #shear_range=0.7,
                                  #zoom_range=[0.9, 2.2],    # 주어진 범위 안에서 축소 또는 회전
                                  #vertical_flip=True,
                                  fill_mode='nearest')      # 이미지를 축소 또는 회전하거나 이동할때 생기는 빈공간 어찌 채울지 정함 nearest하면 가장 비슷한 색으로 채워짐

train_generator = train_datagen.flow_from_directory(
       './train',   #학습셋이 있는 폴더의 위치입니다.
       target_size=(150, 150),
       batch_size=5,
       class_mode='binary')

#테스트 셋은 이미지 부풀리기 과정을 진행하지 않습니다.
test_datagen = ImageDataGenerator(rescale=1./255)  

test_generator = test_datagen.flow_from_directory(
       './test',   #테스트셋이 있는 폴더의 위치입니다.
       target_size=(150, 150), # 이미지크기
       batch_size=5,
       class_mode='binary') # 2진분류 이므로 바이너리 모드 실행


# 앞서 배운 CNN 모델을 만들어 적용해 보겠습니다.
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150,150,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Activation('softmax'))

#모델을 컴파일 합니다. 
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizers.Adam(learning_rate=0.0002), metrics=['accuracy'])

#모델을 실행합니다
history = model.fit_generator(
       train_generator,
       steps_per_epoch=100,
       epochs=20,
       validation_data=test_generator,
       validation_steps=10)

#결과를 그래프로 표현하는 부분입니다.
acc= history.history['accuracy']
val_acc= history.history['val_accuracy']
y_vloss = history.history['val_loss']
y_loss = history.history['loss']

x_len = np.arange(len(y_loss))  
plt.plot(x_len, acc, marker='.', c="red", label='Trainset_acc')
plt.plot(x_len, val_acc, marker='.', c="lightcoral", label='Testset_acc')
plt.plot(x_len, y_vloss, marker='.', c="cornflowerblue", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

plt.legend(loc='upper right') 
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss/acc')
plt.show()


# 전이 학습으로 모델 극대화 하기 : 1. 대규모 데이터 셋에서 학습된 기존의 네트워크 불러온다.  2. cnn모델의 앞쪽을 네트워크로 채운다, 3. 뒤쪽 레이어에서 나의 프로젝트와 연결한다

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import Input, models, layers, optimizers, metrics
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications import VGG16

np.random.seed(3)
tf.compat.v1.set_random_seed(3)

train_datagen = ImageDataGenerator(rescale=1./255,
                                  horizontal_flip=True,
                                  width_shift_range=0.1,
                                  height_shift_range=0.1,
                                  fill_mode='nearest')

train_generator = train_datagen.flow_from_directory(
       'train',
       target_size=(150, 150),
       batch_size=5,
       class_mode='binary')

test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
       'test',
       target_size=(150, 150),
       batch_size=5,
       class_mode='binary')

transfer_model = VGG16(weights='imagenet', include_top=False, input_shape=(150, 150, 3)) # 인클루드 탑, 마지막 분류층을 불러올지 말지 정한다 로컬 네트워크 연결할거 아니면 연결 x, 
transfer_model.trainable = False # 새롭게 학습될거 아니니까 여기도 false
transfer_model.summary()

finetune_model = models.Sequential()
finetune_model.add(transfer_model)
finetune_model.add(Flatten())
finetune_model.add(Dense(64, activation='relu'))
finetune_model.add(Dense(2, activation='softmax'))
finetune_model.summary()

finetune_model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizers.Adam(learning_rate=0.0002), metrics=['accuracy'])

history = finetune_model.fit_generator(
       train_generator,
       steps_per_epoch=100,
       epochs=20,
       validation_data=test_generator,
       validation_steps=4)

acc= history.history['accuracy']
val_acc= history.history['val_accuracy']
y_vloss = history.history['val_loss']
y_loss = history.history['loss']

# 그래프로 표현
x_len = np.arange(len(y_loss))
plt.plot(x_len, acc, marker='.', c="red", label='Trainset_acc')
plt.plot(x_len, val_acc, marker='.', c="lightcoral", label='Testset_acc')
plt.plot(x_len, y_vloss, marker='.', c="cornflowerblue", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss/acc')
plt.show()