# 전국의 대학교 위치를 folium이라는 지도 시각화 라이브러리를 활용하여 지도에 표시
# pip install folium 지도를 시각화 할 수 있다.
# pip install openpyxl
# ---------------------------------------------------------------------------------

# 엑셀 파일을 판다스에서 불러와 학교명과 주소를 찾는 코드 만들기

# import pandas as pd

# filePath = r'.\고등교육기관 하반기 주소록(2020).xlsx'
# df_from_excel = pd.read_excel(filePath,engine='openpyxl')

# df_from_excel.columns = df_from_excel.loc[4].tolist()

# df_from_excel = df_from_excel.drop(index=list(range(0,5))) # 0-5줄의 데이터 버림

# print(df_from_excel.head())

# print(df_from_excel['학교명'].values)

# print(df_from_excel['주소'].values)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# 오픈 api를 이용해 주소를 좌표로 변환하는 코드 만들기

# import requests

# url = 'http://api.vworld.kr/req/address?'
# params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&address=%ED%9A%A8%EB%A0%B9%EB%A1%9C72%EA%B8%B8%2060&refine=true&simple=false&format=xml&type'
# road_type = 'ROAD'
# road_type2 = 'PARCEL'
# address = '&address='
# keys = '&key='
# prikey= '3C9089F6-CD94-3B5C-9501-289CB6FF0187'

# def request_geo(road):
#     page = requests.get(url+params+road_type+address+road+keys+prikey)
#     json_data = page.json()
#     if json_data['response']['status'] == 'OK':
#         x = json_data['response']['result']['point']['x']
#         y = json_data['response']['result']['point']['y']
#         return x,y
#     else:
#         x = 0
#         y = 0
#         return x,y

# x,y = request_geo("경기도 시흥시 산기대학로 237 (정왕동, 한국산업기술대학교)")

# print(f'x값: {x}')
# print(f'y값: {y}')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# 엑셀에서 읽은 학교명과 주소 데이터 api를 통해 x,y좌표를 변경하고 변경된 값을 엑셀파일로 생성

# import pandas as pd
# import requests
# from openpyxl import load_workbook
# from openpyxl import Workbook
# import re

# # 판다스로 읽어옴
# filePath = r'.\고등교육기관 하반기 주소록(2020).xlsx'
# df_from_excel = pd.read_excel(filePath,engine='openpyxl')
# df_from_excel.columns = df_from_excel.loc[4].tolist() 
# df_from_excel = df_from_excel.drop(index=list(range(0,5)))


# url = 'http://api.vworld.kr/req/address?'
# params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
# road_type = 'ROAD'   #도로명주소
# road_type2 = 'PARCEL' #지번주소
# address = '&address='
# keys = '&key='
# primary_key = '3C9089F6-CD94-3B5C-9501-289CB6FF0187'

# # 주소를 좌표로 변환하는 함수
# def request_geo(road):
#     page = requests.get(url+params+road_type+address+road+keys+primary_key)
#     json_data = page.json()
#     if json_data['response']['status'] == 'OK':
#         x = json_data['response']['result']['point']['x']
#         y = json_data['response']['result']['point']['y']
#         return x,y
#     else:
#         x = 0
#         y = 0
#         return x,y

# # 엑셀 파일을 생성한 후 저장
# try:
#     wb = load_workbook(r".\학교주소좌표.xlsx", data_only=True)
#     sheet  = wb.active
# except:
#     wb = Workbook()
#     sheet = wb.active

# university_list = df_from_excel['학교명'].to_list()
# address_list = df_from_excel['주소'].to_list()

# for num,value in enumerate(address_list):
#     addr = re.sub(r'\([^)]*\)', '', value) # 정규식으로 주소의 괄호부분  삭제
#     print(addr)
#     x,y = request_geo(addr) # api를 활용하여 주소를 좌표로 변환
#     sheet.append([university_list[num],addr,x,y]) # 학교명,주소,x,y 순서대로 엑셀에 저장

# wb.save(r".\학교주소좌표.xlsx")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# folium을 이용하여 특정 학교 위치에 마커를 표시

# import folium

# map = folium.Map(location=[37,127],zoom_start=7) # 처음보여주는 위도와 경도 설정, 7은 지도의 배율

# marker = folium.Marker([37.341435483, 126.733026596],
#                     popup='한국공학대학교', 
#                     icon = folium.Icon(color='blue')) # 파란색으로 마커 표시

# marker.add_to(map)  # 마커 추가

# map.save(r'./uni_map.html')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# 전국의 모든 대학교 위치 시각화

import pandas as pd
import folium

filePath = r'.\학교주소좌표.xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl',header=None) 

df_from_excel.columns = ['학교이름','주소','x','y'] # 컬럼을 학교이름,주소,x,y로 정함

name_list = df_from_excel['학교이름'].to_list() # dataframe을 to_list() 함수를 이용하여 리스트로 변환
addr_list = df_from_excel['주소'].to_list()
position_x_list = df_from_excel['x'].to_list()
position_y_list = df_from_excel['y'].to_list()

map = folium.Map(location=[37,127],zoom_start=7) # 기본 맵 설정

for i in range(len(name_list)): # 학교 이름만큼 반복
    if position_x_list[i] != 0:
        marker = folium.Marker([position_y_list[i],position_x_list[i]],
                            popup=name_list[i], 
                            icon = folium.Icon(color='blue'))
        marker.add_to(map) 

map.save(r'./uni_map.html')