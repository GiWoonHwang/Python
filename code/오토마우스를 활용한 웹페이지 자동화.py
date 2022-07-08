# 자동으로 마우스와 키보드를 조작하는 코드를 작성하여 웹페이지에서 자동을로 날씨 정보를 얻는 프로그램을 만들어보자
# pip install pyautogui
# pip install pyperclip  클립보드에 값을 복사하거나 붙여넣기 용도로 사용

# 꿀팁 모음
# pyautogui.position() 마우스의 좌표 입력받음
# .moveTo(x,y) 절대좌표로 이동
# .moveTO(x,y,시간) 정해진 좌표로 지정된 시간동안 이동
# .moveRel(x,y) 현재 마우스 위치로부터 x,y 픽셀만큼 이동
# .click() 현재 마우스 커서 위치에 마우스를 클릭
# .doubleClick() 현재 마우스 위치에 마우스를 더블클릭
# .click(50,50) 이 위치에 마우스를 클릭
# .click(x=50, y=50) 이 좌표위치에 마우스 클릭, 위에 모듈이랑 무슨차인지 모르겠음
# .rightClick() 현재 위치에 마우스를 우클릭
# .dragTo(x=50,y=50, duration=2) 현재 위치부터 좌표까지 2초동안 드래그
# .typewrite('ABC') ABC를 입력한다 한글은 지원되지 않는다. 한글은 pyperclip 라이브러리를 이용하여 붙여넣기를 통해 입력한다
# .typewrite('ABC', interval=1) # 1초동안 입력
# .hotkey('ctrl', 'V') 두개의 키를 동시에 누름
# .screenshot('저장경로', region=(100,100,50,50)) 스크린샷을 이용하여 부분캡쳐 진행, x,y좌표 및 가로세로 사이즈이다.

# import pyautogui
# import time

# while True:
#     print(pyautogui.position()) # 마우스의 좌표 출력
#     time.sleep(0.1)
# ---------------------------------------------------------------------------------------------------

# 네이버에서 자동으로 서울 날씨 검색하는 코드 만들기

# import pyautogui
# import time
# import pyperclip

# pyautogui.moveTo(1235,245,0.2) # 좌표로 0.2초동안 이동
# pyautogui.click()
# time.sleep(0.5) # 대기

# pyperclip.copy('서울날씨') # 클립보드에 텍스트 저장
# pyautogui.hotkey('ctrl', 'v') # 클립보드에 있는거 붙여넣기
# time.sleep(0.5) # 대기

# pyautogui.write(['enter']) # 엔터입력
# time.sleep(1)
# ---------------------------------------------------------------------------------------------------

# 오토마우스를 활용환 웹페이지 자동화

# import pyautogui
# import time
# import pyperclip

# pyautogui.moveTo(1235,245,0.2) # 좌표로 0.2초동안 이동
# pyautogui.click()
# time.sleep(0.5) # 대기

# pyperclip.copy('서울날씨') # 클립보드에 텍스트 저장
# pyautogui.hotkey('ctrl', 'v') # 클립보드에 있는거 붙여넣기
# time.sleep(0.5) # 대기

# pyautogui.write(['enter']) # 엔터입력
# time.sleep(1)

# start_x = 994
# start_y = 260

# end_x = 1654
# end_y = 651

# pyautogui.screenshot(r'./서울날씨.png', region=(start_x,start_y, end_x-start_x, end_y-start_y))
# # 시작좌표x, 시작좌표y 크기x, 크기y(크기는 뺼셈으로 구함)
# ----------------------------------------------------------------------------------------

# 여러 지역 날씨를 자동으로 검색 후 저장하는 코드 만들기

import pyautogui
import time
import pyperclip

날씨 = ['서울날씨','시흥날씨','청주날씨','부산날씨','강원도날씨']

addr_x = 1105
addr_y = 63
start_x = 994
start_y = 260
end_x = 1654
end_y = 651

for 지역날씨 in 날씨:
    pyautogui.moveTo(addr_x,addr_y,1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write('www.naver.com', interval=0.1)
    pyautogui.write(['enter'])
    time.sleep(1)
    
    pyperclip.copy(지역날씨)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.5)
    pyautogui.write(['enter'])
    time.sleep(1)
    저장경로 = ('./'+ 지역날씨 + '.png')
    pyautogui.screenshot(저장경로, region=(start_x,start_y, end_x-start_x, end_y-start_y))