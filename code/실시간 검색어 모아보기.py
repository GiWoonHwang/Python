# 어떤 이슈들이 있는지 궁금할 때 실시간 검색어를 모아볼 수 있는 프로그램을 만들어 본다.
# pip install selenium
# pip install webdriver-manager
# 구글 크롬 브라우저 설치

# 파이썬으로 제어할 수 있는 크롬창을 띄움
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install()) 

url = 'https://www.google.co.kr'
driver.get(url=url)
driver.implicitly_wait(time_to_wait=10)
# ---------------------------------------------------------------------------------------
url = 'https://signal.bz/news'
driver.get(url=url)
driver.implicitly_wait(time_to_wait=10)

naver_results = driver.find_element_by_css_selector('')

naver_list = []
for naver_result in naver_results:
    print(naver_result.text) 
    naver_list.append(naver_result.text) # 찾은 원소중에서 text만 추출하여 리스트에 넣음
