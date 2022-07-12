# tkinter를 이용하여 간단한 gui 프로그램을 만들어 실시간 가상 금액을 표시해보자
# pip install pyupbit

# import tkinter

# window = tkinter.Tk() # 윈도우 객체 생성
# window.title('가상화폐 금액 표시') # 타이틀
# window.geometry('400x200') # 사이즈 조절
# window.resizable(False,False) # 가로세로 고정시킴

# label = tkinter.Label(window, text='hello') # 문자열 출력
# label.pack()

# window.mainloop()

# ---------------------------------------------------------------------------------------------

# hello 글자 크기를 키우는 코드 만들기

# import tkinter
# import tkinter.font

# window = tkinter.Tk()
# window.title('가상화폐 금액 표시')
# window.geometry('400x200')
# window.resizable(False,False)

# font = tkinter.font.Font(size = 30)
# label = tkinter.Label(window, text='hello', font=font)
# label.pack()

# window.mainloop()
# ---------------------------------------------------------------------------------------------

# 1초마다 반복해서 동작하는 코드 만들기

# import tkinter
# import tkinter.font

# window = tkinter.Tk()
# window.title("가상화폐 금액표시")
# window.geometry("400x200")
# window.resizable(False,False)

# font = tkinter.font.Font(size = 30)
# label=tkinter.Label(window, text="", font=font)
# label.pack()

# cnt = 0
# def get_coin_1sec():
#     global cnt
#     now_btc_price = str(cnt)
#     cnt = cnt + 1
#     label.config(text=now_btc_price)
#     window.after(1000,get_coin_1sec) # 1초후에 함수를 불러온다. 1000ms 즉 1초이다

# get_coin_1sec()

# window.mainloop()
# ---------------------------------------------------------------------------------------------

# 1초마다 반복해서 동작하는 gui 코드 만들기
# exe 파일 만들기 팁 : 통합 터미널에서 연 후 pyinstaller -w -F 파일이름.py

import tkinter
import tkinter.font
import pyupbit
import threading
import time

coin_price = 0

# 실시간 비트코인 데이터를 가져와 coin_price에 저장 그 후 쓰레드 처리했음 
def get_coin_price():
    global coin_price
    while True:
        coin_price = pyupbit.get_current_price("KRW-BTC")
        time.sleep(1.0)
        
t1 = threading.Thread(target=get_coin_price)
t1.daemon = True
t1.start()

window = tkinter.Tk()
window.title("비트코인 실시간 가격")
window.geometry("400x50")
window.resizable(False,False)

font = tkinter.font.Font(size = 30)
label=tkinter.Label(window, text="", font=font)
label.pack()

def get_coin_1sec():
    global coin_price
    now_btc_price = str(coin_price)
    label.config(text=now_btc_price)
    window.after(1000,get_coin_1sec)

get_coin_1sec()

window.mainloop()