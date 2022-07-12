# 랜덤한 번호를 추출하여 로또번호를 생성하는 gui 프로그램 만들기

# import random

# lotto_num = range(1,46)

# for i in range(5):
#     print(random.sample(lotto_num,6))
# -----------------------------------------------------------------------------------------------------------------------------------------------

# 로또 번호를 생성하는 gui 프로그램 만들기

# import tkinter
# import tkinter.font
# import random

# lotto_num = range(1,46)

# def buttonClick():
#     print(random.sample(lotto_num,6))
    
# window = tkinter.Tk()
# window.title('lotto')
# window.geometry('400x200+800+300') # 크기와 초기 좌표를 나타냄
# window.resizable(False,False)



# button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
# button.pack()

# window.mainloop()
# -----------------------------------------------------------------------------------------------------------------------------------------------

# 이제 생성한 번호를 gui에도 출력해보자

import tkinter
import tkinter.font
import random

lotto_num = range(1,46)

def buttonClick():
    for i in range(5):
        lottoPick = map(str,random.sample(lotto_num,6)) # 생성된 번호 6개를 맵함수를 이용하여 문자열로 변환
        lottoPick = ','.join(lottoPick) # join함수를 이용하여 변환된 문자열에 ,넣어줌
        lottoPick = str(i+1) + "회: " + lottoPick
        print(lottoPick)
        listbox.insert(i, lottoPick)
    listbox.pack()
    
window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200+800+300")
window.resizable(False, False)

button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

font = tkinter.font.Font(size = 20)
listbox = tkinter.Listbox(window, selectmode='extended', height=5, font=font)
listbox.insert(0, "1회:")
listbox.insert(1, "2회:")
listbox.insert(2, "3회:")
listbox.insert(3, "4회:")
listbox.insert(4, "5회:")
listbox.pack()

window.mainloop()