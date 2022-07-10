# 구글 사이트에서 이미지를 검색하고 저장하는 로직 작성
# 크롤링은 py보다 주피터 노트북 형식인 ipynb가 좋다 우리가 크롤링하는 대부분의 사이트는 사람이 아닌 기계로 접속하는것을 꺼려하기 때문
# pip install selenium 웹을 제어하는 라이브러리
# pip install webdriver-manager 웹 드라이버에 사용하는 크롬 드라이버 파일을 손쉽게 다운로드 할 수 있는 라이브러리

from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동설치를 위한 라이브러리 불러옴
from selenium import webdriver # 크롬드라이버 제어를 위한 라이브러리 불러옴

driver = webdriver.Chrome(ChromeDriverManager().install()) # 크롬드라이버 시작함

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)

# 코드가 실행되고 이미지 검색 사이트로 접속된다. 실행한 이 코드를 중단하지 말고 다음 코드를 작성한다
# --------------------------------------------------------------------------------------------------------

from selenium.webdriver.common.keys import Keys

elem = driver.find_element_by_css_selector('#sbtc>div>div.a4bic>input') # 원소를 찾음
elem.send_keys('바다') # 검색할 사진인 바다를 입력
elem.send_keys(Keys.RETURN) # 엔터키를 입력하여 검색
# --------------------------------------------------------------------------------------------------------

import time
elem = driver.find_element_by_tag_name('body') # 바다부분을 찾는다
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN) # 페이지 다운키를 60번 눌러 사진이 계속 보이게 함
    time.sleep(0.1)

try:
    driver.find_element_by_css_selecotr('#islmp>div>div>div>div.gBPMB>div.qvfT1>div.YstHxe>input').click() # 중간에 결과 더보기 버튼이 있다면 눌러서 계속 사진 보이게 함

    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass
# --------------------------------------------------------------------------------------------------------

links = []

images = driver.find_element_by_css_selecotr('') # 이미지의 원소를 모두 찾는다

for image in images: # 찾은 이미지 수 만큼 반복한다
    if image.get_attribute('src') is not None: # 링크 주소가 존재한다면
        links.append(image.get_attribute('src')) # 리스트에 추가

print('찾은 이미지 개수:', len(links))
# --------------------------------------------------------------------------------------------------------

import urllib.request # 사진을 다운받기 위해 request 라이브러리 불러옴

for k,i in enumerate(links): # 넘어온 목록을 기준으로 인덱스와 원소를 차례로 접근하게 해준다.
    url = i
    urllib.request.urlretrieve(url, '저장한 경로')

print('다운완료')