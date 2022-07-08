# 오토마우스를 활용하여 pc에 설치된 카카오톡을 통해 메시지를 자동으로 보내는 프로그램을 만들어본다
# pip install pyautogui
# pip install pyperclip
# pip install schedule 일정시간마다 함수를 동작시킨다

# import pyautogui
# import os

# os.chdir(os.path.dirname(os.path.abspath(__file__))) # 경로를 현재 .py파일을 실행하는 경로로 이동한다. pyautogui에서 한글을 인식하지 못해 경로를 이동

# picPosition = pyautogui.locateOnScreen('pic1.png') # 파일과 동일한 그림의 좌표를 찾아 이동
# print(picPosition)

# if picPosition is None:
#     picPosition = pyautogui.locateOnScreen('pic2.png')
#     print(picPosition)

# if picPosition is None:
#     picPosition = pyautogui.locateOnScreen('pic3.png')
#     print(picPosition)
# -----------------------------------------------------------------------------------------------------------------------------------------

# 찾은 좌표를 이용하여 메시지를 자동으로 보내는 프로그램

# import pyautogui
# import os
# import time
# import pyperclip

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# picPosition = pyautogui.locateOnScreen('pic1.png') # 파일과 동일한 그림의 좌표를 찾아 이동
# print(picPosition)

# if picPosition is None:
#     picPosition = pyautogui.locateOnScreen('pic2.png')
#     print(picPosition)

# if picPosition is None:
#     picPosition = pyautogui.locateOnScreen('pic3.png')
#     print(picPosition)

# clickPosition = pyautogui.center(picPosition)
# pyautogui.doubleClick(clickPosition)

# pyperclip.copy('서현식')
# pyautogui.hotkey('ctrl', 'v')
# time.sleep(1.0)

# pyautogui.write(['enter'])
# time.sleep(1.0)

# pyautogui.write(['escape'])
# time.sleep(1.0)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# 일정시간마다 동작하는 코드 만들기. 파이썬의 tread 기능을 이용하여 자기 자신의 함수를 호출하는 코드 만들기

# import pyautogui
# import pyperclip
# import time
# import os
# import threading

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# def send_message(): # 카카오톡을 보내는 기능을 함수로 만들었다.
#     threading.Timer(10, send_message).start() # 함수를 10초후에 실해한다. 자신의 함수에서 10초후에 자신의 함수를 불러오기 때문에 10초마다 실행
    
#     picPosition = pyautogui.locateOnScreen('pic1.png') # 파일과 동일한 그림의 좌표를 찾아 이동
#     print(picPosition)

#     if picPosition is None:
#         picPosition = pyautogui.locateOnScreen('pic2.png')
#         print(picPosition)

#     if picPosition is None:
#         picPosition = pyautogui.locateOnScreen('pic3.png')
#         print(picPosition)

#     clickPosition = pyautogui.center(picPosition)
#     pyautogui.doubleClick(clickPosition)

#     pyperclip.copy('서현식')
#     pyautogui.hotkey('ctrl', 'v')
#     time.sleep(1.0)

#     pyautogui.write(['enter'])
#     time.sleep(1.0)

#     pyautogui.write(['escape'])
#     time.sleep(1.0)
    
# send_message() # 처음한번 함수를 실행
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

# 조금 더 편하게 요일, 시간등을 설정하여 보내는 로직을 구현해보자

import pyautogui
import pyperclip
import os
import time
import threading
import schedule

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def send_message(): # 카카오톡을 보내는 기능을 함수로 만들었다.
    # threading.Timer(10, send_message).start() # 함수를 10초후에 실행한다. 자신의 함수에서 10초후에 자신의 함수를 불러오기 때문에 10초마다 실행
    
    picPosition = pyautogui.locateOnScreen('pic1.png') # 파일과 동일한 그림의 좌표를 찾아 이동
    print(picPosition)

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen('pic2.png')
        print(picPosition)

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen('pic3.png')
        print(picPosition)

    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy('서현식')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1.0)

    pyautogui.write(['enter'])
    time.sleep(1.0)

    pyautogui.write(['escape'])
    time.sleep(1.0)


# 스케쥴문을 이용하여 업무 자동화가 가능하다. (반복문 필수)
schedule.every(2).seconds.do(send_message)
schedule.every().monday.at('09:10').do(send_message)
schedule.every().day.at('10:30').do (send_message)

while True:
    schedule.run_pending()
    time.sleep(1.0)