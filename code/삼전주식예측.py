# pip install tensorflow==2.3 인공지능을 사용하기 위한 라이브러리
# pip install keras==2.4.3 텐서플로우를 쉽게 사용하게 해주는 라이브러리
# pip install pandas-datereader 주식 데이터를 판다스 형식으로 가져옴
# pip install yfinace 야후의 주식정보 가져옴

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pandas_datareader import data as pdr
import yfinance as yf # 야후에서 데이터를 획득하는 방식이 크롤링으로 변경되어 주가 데이터 불러옴
yf.pdr_override()
# -----------------------------------------------------------------------------------------------------------

now = datetime.now() # 현재시간 가져옴

before = now - relativedelta(years=10) # 10년전 시간 가져옴

now_day = now.strftime("%Y-%m-%d") # 년 월 일 문자열로 변경
befor_day = before.strftime("%Y-%m-%d")
print(f"end  : {now_day}")
print(f"start: {befor_day}")

# 삼전의 10년치 주식을 판다스의 데이터프레임 형식으로 가져옴, 005930.ks는 삼전주식코드, ks는 한국 주식 시세 가져오는것
samsung_stock = pdr.get_data_yahoo( "005930.KS", start=befor_day, end=now_day)
print(samsung_stock)
# -----------------------------------------------------------------------------------------------------------

# 종가만 가져와서 분리 후 정규화 진행
close_prices = samsung_stock['Close'].values # 종가만 가져옴
print(close_prices)

windown_size = 30

result_list = [] # 데이터를 30개씩 분리해서 담는다
for i in range(len(close_prices) - (windown_size + 1)): # 이거 왜 빼주는지 모르겟음
    result_list.append(close_prices[i: i + (windown_size + 1)])

normal_data = [] # 데이터를 정규화 한다. 첫번 째 데이터를 나눠 폭을 줄인다.
for window in result_list:
    window_list = [((float(p) / float(window[0])) - 1) for p in window]
    normal_data.append(window_list)

result_list = np.array(normal_data)
print(result_list.shape[0], result_list.shape[1])
# -------------------------------------------------------------------------------------------------------------------------------

row = int(round(result_list.shape[0] * 0.9))
train = result_list[:row, :]

x_train = train[:, :-1]
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1]

x_test = result_list[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = result_list[row:, -1]

x_train.shape, x_test.shape
# --------------------------------------------------------------------------------------------

model = Sequential()
model.add(LSTM(windown_size, return_sequences=True, input_shape=(windown_size, 1)))
model.add(LSTM(64, return_sequences=False))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse', optimizer='rmsprop')
model.summary()
# --------------------------------------------------------------------------------------------

model.fit(x_train, y_train,
    validation_data=(x_test, y_test),
    batch_size=10,
    epochs=10)

model.save(r'.\samsung.h5')
# --------------------------------------------------------------------------------------------

pred = model.predict(x_test)

pred_price = []
for i in pred:
    pred_price.append( (i + 1) * window[0] )
    
real_price = []
for i in y_test:
    real_price.append( (i + 1) * window[0] )

fig = plt.figure(facecolor='white', figsize=(70, 15))
ax = fig.add_subplot(234)
ax.plot(real_price, label='real_price')
ax.plot(pred_price, label='pred_price')
ax.legend()
plt.show()