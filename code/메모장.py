# gui를 이용하여 메모장을 만들자

from tkinter import *
from tkinter.filedialog import *

# 메뉴를 선택했을 때 동작하는 함수

def new_file(): # 새 파일을 눌렀을 때 텍스트 영역 지움
    text_area.delete(1.0,END)

def save_file(): # 저장
    f = asksaveasfile(mode = "w", defaultextension=".txt",filetypes=[('Text files', '.txt')])
    text_save = str(text_area.get(1.0, END))
    f.write(text_save)
    f.close()

def maker(): # 만든이 눌렀을 때 새 창 생성 및 내용 표시
    help_view = Toplevel(window)
    help_view.geometry("300x50+800+300")
    help_view.title("만든이")
    lb = Label(help_view, text = "파이썬과 40개의 작품들 메모장 만들기 입니다.")
    lb.pack()

window = Tk()
window.title('메모장')
window.geometry('400x200+800+300')
window.resizable(False,False)

# 새파일, 저장, 종료로 파일안에 묶음
menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label='새파일', command= new_file)
menu_1.add_command(label='저장', command= save_file)
menu_1.add_separator()
menu_1.add_command(label='종료', command=window.destroy)
menu.add_cascade(label='파일', menu=menu_1)

# 만든이 안에 만든이로 묶음
menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label='만든이',command= maker)
menu.add_cascade(label='만든이',menu=menu_2)

# menu_2 = Menu(menu, tearoff=0)
# menu_2.add_command(label="만든이", command = maker)
# menu.add_cascade(label="만든이", menu=menu_2)


text_area = Text(window)
# 왼쪽 오른쪽 공백설정 (이거 유무 잘 모르겠음)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# 텍스트창을 동서남북 방향으로 붙임 이건 꼭 필요함
text_area.grid(sticky = N + E + S + W)

window.config(menu=menu)

window.mainloop()


window.config(menu=menu)
window.mainloop()


