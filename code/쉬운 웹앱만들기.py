# 달력으로 날짜를 선택하여 비트코인의 시세를 한시간 단위로 그래프에 보여주는 웹앱입니다.
# pip install streamlit 설치시 이메일을 입력하는 부분이 출력되면 사용하는 이메일을 입력한다. 업데이트 내용 등을 이메일을 통해 알려줌
# pip install pyupbit
# ----------------------------------------------------------------------------------------------------------------------------

# import streamlit as st

# data_list = {5,5,6,6,7}
# st.write('''
# 샘플데이터
# ''')

# st.line_chart(data_list)
# ----------------------------------------------------------------------------------------------------------------------------

# import streamlit as st
# import datetime

# # 달력으로 날짜를 입력받는다
# d = st.date_input(
#     "날짜를 선택하세요",
#     datetime.date.today())

# # 선택한 날짜 출력
# st.write('선택한 날짜:',d)
# ----------------------------------------------------------------------------------------------------------------------------

# 선택한 날짜의 비트코인 시세를 그래프로 출력해주는 코드 만들기

import streamlit as st
import datetime
import pyupbit

d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today())

st.write('비트코인 1일 차트')

ticker = 'KRW-BTC'
interval = 'minute60'
to = str(d + datetime.timedelta(days=1)) # 입력한 날짜에 하루를 더해준다. 이전데이터 24개를 가지고 오기 때문에 5일의 값을 알고싶다면 6일부터 이전 24개 데이터를 가져오면 됨
count = 24
price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

st.line_chart(price_now.close) # 그래프로 그려줌