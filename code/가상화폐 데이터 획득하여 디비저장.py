# 가상화폐 데이터를 db에 저장
# pip install pyupbit
# SQLite 설치

# import pyupbit

# coin_lists = pyupbit.get_tickers(fiat='KRW')
# print(coin_lists)

# price_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
# print(price_now)
#---------------------------------------------------------------------------------------------------------------------------------

# 비트코인의 분봉값을 db에 저장 

# import pyupbit
# import sqlite3

# ticker = 'KRW-BTC' # 한화로 비트코인 불러옴
# interval = 'minute1' # 분봉 데이터 불러오기
# to = '2021-12-02 11:20' # 이 시간 이전 데이터 불러온다
# count = 200 # 200개
# price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

# db_path = r".\coin.db"

# con = sqlite3.connect(db_path, isolation_level=None) # db데이터 생성, isolation_level = 특정 트랜잭션이 다른 트랜잭션에서 변경하거나 조회하는 데이터를 볼 수 있도록 허용할지 말지를 결정하는 것.
# price_now.to_sql('BTC', con, if_exists='append') # btc이름으로 데이터 생성 후 데이터 추가 # 데이터베이스에 테이블이 존재할 때 수행 동작을 지정한다. 'fail', 'replace', 'append' 중 하나를 사용할 수 있는데 기본값은 'fail'이다. 'fail'은 데이터베이스에 테이블이 있다면 아무 동작도 수행하지 않는다. 'replace'는 테이블이 존재하면 기존 테이블을 삭제하고 새로 테이블을 생성한 후 데이터를 삽입한다. 'append'는 테이블이 존재하면 데이터만을 추가한다.

# con.close
#---------------------------------------------------------------------------------------------------------------------------------

# 판다스 라이브러리를 불러와 db의 btc 데이터를 읽는다.
# import pandas as pd
# import sqlite3

# db_path = r".\coin.db"
# con = sqlite3.connect(db_path, isolation_level=None)

# readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col = 'index')

# print(readed_df)
#---------------------------------------------------------------------------------------------------------------------------------

import pyupbit
import sqlite3
import datetime

def date_range(start, end): # 시작과 종료날짜를 리스트로 반환
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    start = start + datetime.timedelta(days=1)
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    end = end + datetime.timedelta(days=1) 
    dates = [(start + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates = date_range("2021-11-30", "2021-12-01")

print(dates)

for day in reversed(dates): # 날짜를 뒤집어 최신날짜부터
    myDay = day + ' 00:00'
    print(myDay)

    ticker = 'KRW-BTC'
    interval = 'minute1'
    to = myDay
    count = 1440 
    price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

    print(price_now)

    db_path = r"25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"

    con = sqlite3.connect(db_path, isolation_level=None)
    price_now.to_sql('BTC', con, if_exists='append')  

    con.close
#---------------------------------------------------------------------------------------------------------------------------------

# db의 중복 제거 코드

import pandas as pd
import sqlite3

db_path = r".\coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT DISTINCT * FROM 'BTC'", con, index_col = 'index')

readed_df.to_sql('BTC_NEW', con, if_exists='replace')

print(readed_df)
