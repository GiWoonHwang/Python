# 핫딜사이트에서 내가 원하는 제품 키워드를 검색하여 스마트폰으로 알려주는 프로그램 만들기
# pip install selenium
# pip install webriver-manager
# pip install python-telegram-bot
# 구글 크롬 설치
# 뽐뿌 사이트 이용

from turtle import title
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
driver.implicitly_wait(time_to_wait=10) 
# ----------------------------------------------------------------------------------------------

# 뽐뿌 게시판에서 글과, 링크 주소를 찾는 코드
title = driver.find_element_by_css_selctor('') # 게시글 제목을 찾음
urls = driver.find_element_by_css_selctor('') # 게시글 링크 주소를 찾음

for i in range(len(title)): # 제목과 링크 주소 출력
    print(title[i].text)
    print(urls[i].get_attribute('href'))
# ----------------------------------------------------------------------------------------------

# 위에서 출려된 제목중 '김치'가 포함되어 있다면 텔레로 메세지를 보내는 로직 작성

import telegram
message = ''
for i in range(len(title)):
    if '김치' in title[i].text:
        message = title[i].text + '\n' + urls[i].get_attribute('href') # 보내는 메세지는 제목 + 링크
        print(message)
        token = '텔레 토큰'
        id = '텔레 아디'
        bot = telegram.Bot(token)
        bot.sendMessage(chat_id = id, text = message)
# ----------------------------------------------------------------------------------------------

# 반복적으로 게시판을 보고 있다가 찾는 키워드가 있으면 스마트폰으로 알림을 보내는 코드 작성

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import telegram
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
send_message_list = [] # 보낸 메세지를 기록하는 리스트 만듬

while True: # 반복
    try:
        driver.get(url=urls)
        titles = driver.find_elements_by_css_selector('') # 뽐뿌 사이트 접속하게 제목과 링크 주소를 찾음
        urls = driver.find_elements_by_css_selector('')
        mesage=''
        for i in range(len(titles)):
            mesage = title[i].text + '\n' + urls[i].get_attribute('href')
            if message not in send_message_list:
                print(message)
                send_message_list.append(message)
                token = ''
                id = ''
                bot = telegram.Bot(token)
                bot.sendMessage(chat_id = id, text= message)
        time.sleep(60.0 * 5)
    except KeyboardInterrupt:
        break

        

