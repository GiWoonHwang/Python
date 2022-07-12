# 로또 당첨번호의 엑셀 파일을 읽어 파이썬을 통해 시각화 하는 프로그램 만들기
# pip install openpyxl
#------------------------------------------------------------------------------------------------

# 엑셀 파일을 판다스로 읽음

# import openpyxl
# import pandas as pd

# file_path = r'.\lotto.xlsx'
# df_from_excel = pd.read_excel(file_path, engine='openpyxl') # 판다스의 데이터프레임으로 엑셀파일 불러옴
# # df_from_excel = df_from_excel.drop(index=[0,1]) #  0,1 삭제함 사실 안해도 되는데 하느게 깔끔함

# df_from_excel.columns = [ # 컬럼을 다시 정의
#                         '년도', '회차','추첨일','1등당첨자수',
#                         '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
#                         '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
#                         '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
#                         '당첨번호4','당첨번호5','당첨번호6','보너스번호'
#                         ]

# print(df_from_excel.head()) # 앞부분의 데이터만 출력
# print(df_from_excel['회차'].values) # 회차 출력
# print(df_from_excel['1등당첨금액'].values)
#------------------------------------------------------------------------------------------------

# 그래프로 그림

# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc

# file_path = r'.\lotto.xlsx'
# df_from_excel = pd.read_excel(file_path,engine='openpyxl')

# df_from_excel = df_from_excel.drop(index=[0,1])

# df_from_excel.columns = [
#                         '년도', '회차','추첨일','1등당첨자수',
#                         '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
#                         '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
#                         '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
#                         '당첨번호4','당첨번호5','당첨번호6','보너스번호'
#                         ]
# # 엑셀 파일의 당첨금액 ', + 원'을  삭제한다
# df_from_excel['1등당첨금액']=df_from_excel['1등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True) 
# df_from_excel['2등당첨금액']=df_from_excel['2등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
# df_from_excel['3등당첨금액']=df_from_excel['3등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
# df_from_excel['4등당첨금액']=df_from_excel['4등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
# df_from_excel['5등당첨금액']=df_from_excel['5등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)

# df_from_excel["1등당첨금액"] = pd.to_numeric(df_from_excel["1등당첨금액"]) # 값을 다시 숫자형태로 데이터 프레임에 저장함
# df_from_excel["2등당첨금액"] = pd.to_numeric(df_from_excel["2등당첨금액"])
# df_from_excel["3등당첨금액"] = pd.to_numeric(df_from_excel["3등당첨금액"])
# df_from_excel["4등당첨금액"] = pd.to_numeric(df_from_excel["4등당첨금액"])
# df_from_excel["5등당첨금액"] = pd.to_numeric(df_from_excel["5등당첨금액"])

# print( df_from_excel[['1등당첨금액','2등당첨금액','3등당첨금액','4등당첨금액','5등당첨금액']] )

# font_path = "C:/Windows/Fonts/Corbel.TTF" # 그래프에 쓸 한글폰틀르 지정
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

# x = df_from_excel['회차'].iloc[:100].values # 회차의 마지막 100개의 데이터만 x축으로 사용
# price = df_from_excel['1등당첨금액'].iloc[:100].values / 100000000 # 당첨금액의 마지막  100개 데이터만 y축으로 사용 나눠준 이유는 억원으로 표시하기 위해

# plt.figure(figsize=(10, 5)) # 그래프의 초기 크기 결정
# plt.xlabel('회차') 
# plt.ylabel('당첨금액(단위:억원)') 

# plt.bar(x, price, width=0.4) # 바의 x,y 값과 폭 지정

# plt.show()
#------------------------------------------------------------------------------------------------

# 당첨번호의 빈도수를 출력하는 코드 만들기

import openpyxl
import pandas as pd
from collections import Counter

file_path = r'.\lotto.xlsx'
df_from_excel = pd.read_excel(file_path, engine='openpyxl')
df_from_excel = df_from_excel.drop(index=[0,1])

df_from_excel.columns = [
                        '년도', '회차','추첨일','1등당첨자수',
                        '1등당첨금액','2등당첨자수','2등당첨금액','3등당첨자수',
                        '3등당첨금액','4등당첨자수','4등당첨금액','5등당첨자수',
                        '5등당첨금액','당첨번호1','당첨번호2','당첨번호3',
                        '당첨번호4','당첨번호5','당첨번호6','보너스번호'
                        ]

# 6개의 번호를 숫자형 타입으로 읽어 리스트에 저장
num_list = list(df_from_excel['당첨번호1'].astype(int))
num_list += list(df_from_excel['당첨번호2'].astype(int))
num_list += list(df_from_excel['당첨번호3'].astype(int))
num_list += list(df_from_excel['당첨번호4'].astype(int))
num_list += list(df_from_excel['당첨번호5'].astype(int))
num_list += list(df_from_excel['당첨번호6'].astype(int))

count = Counter(num_list)
most_num = count.most_common(45) # 가장 많이나온 숫자 45개를 찾음

print(most_num)

