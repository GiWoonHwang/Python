# pyqt의 gui 라이브러리를 활용하여 럭키 계산기 만들어보기
# 새 터미널 열어서 designer 입력

# import sys 
# from PyQt5.QtWidgets import *
# from PyQt5 import uic


# ui_path = r".\계산기.ui"
# form_class = uic.loadUiType(ui_path)[0] 


# class WindowClass(QMainWindow, form_class) : # form_class부터 상속받은 자식 클래스이다 form_class은 계산기 ui이다
#     def __init__(self) :
#         super().__init__() # 부모 클래스 초기화
#         self.setupUi(self)


# if __name__ == "__main__" :
#     app = QApplication(sys.argv)  # 계산기 gui 불러온다
#     myWindow = WindowClass() 
#     myWindow.show() 
#     app.exec_()
# -------------------------------------------------------------------------------------------------

# 계산기에 기능을 추가해보자. 터미널에 출력

# import sys 
# from PyQt5.QtWidgets import *
# from PyQt5 import uic


# ui_path = r"33. 계산기 만들기(PYQT)\계산기.ui"
# form_class = uic.loadUiType(ui_path)[0] 


# class WindowClass(QMainWindow, form_class) : 
#     def __init__(self) :
#         super().__init__()
#         self.setupUi(self)

#         self.btn_C.clicked.connect(self.btn_clicked)
#         self.btn_number0.clicked.connect(self.btn_clicked)
#         self.btn_number1.clicked.connect(self.btn_clicked)
#         self.btn_number2.clicked.connect(self.btn_clicked)
#         self.btn_number3.clicked.connect(self.btn_clicked)
#         self.btn_number4.clicked.connect(self.btn_clicked)
#         self.btn_number5.clicked.connect(self.btn_clicked)
#         self.btn_number6.clicked.connect(self.btn_clicked)
#         self.btn_number7.clicked.connect(self.btn_clicked)
#         self.btn_number8.clicked.connect(self.btn_clicked)
#         self.btn_number9.clicked.connect(self.btn_clicked)
#         self.btn_result.clicked.connect(self.btn_clicked)
#         self.btn_minus.clicked.connect(self.btn_clicked)
#         self.btn_add.clicked.connect(self.btn_clicked)
#         self.btn_multipy.clicked.connect(self.btn_clicked)
#         self.btn_divide.clicked.connect(self.btn_clicked)

#         self.le_view.setEnabled(False) # 글을 입력하지 못하게 함
        
#     def btn_clicked(self):
#         btn_value = self.sender().text()
#         print(btn_value)

# if __name__ == "__main__" :
#     app = QApplication(sys.argv) 
#     myWindow = WindowClass() 
#     myWindow.show() 
#     app.exec_()
# -------------------------------------------------------------------------------------------------

# 계산기에 수식을 추가해보자

import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic


ui_path = r".\계산기.ui"
form_class = uic.loadUiType(ui_path)[0] 


class WindowClass(QMainWindow, form_class) : 
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn_C.clicked.connect(self.btn_clicked)
        self.btn_number0.clicked.connect(self.btn_clicked)
        self.btn_number1.clicked.connect(self.btn_clicked)
        self.btn_number2.clicked.connect(self.btn_clicked)
        self.btn_number3.clicked.connect(self.btn_clicked)
        self.btn_number4.clicked.connect(self.btn_clicked)
        self.btn_number5.clicked.connect(self.btn_clicked)
        self.btn_number6.clicked.connect(self.btn_clicked)
        self.btn_number7.clicked.connect(self.btn_clicked)
        self.btn_number8.clicked.connect(self.btn_clicked)
        self.btn_number9.clicked.connect(self.btn_clicked)
        self.btn_result.clicked.connect(self.btn_clicked)
        self.btn_minus.clicked.connect(self.btn_clicked)
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_multipy.clicked.connect(self.btn_clicked)
        self.btn_divide.clicked.connect(self.btn_clicked)

        self.le_view.setEnabled(False)
        
        self.text_value = ""
        
    def btn_clicked(self):
        btn_value = self.sender().text()
        if btn_value == 'C': # c버튼 눌리면 초기화
            print("clear")
            self.le_view.setText("0")
            self.text_value = ""
        elif btn_value == '=': # 이거눌리면 값 보여줌 .lstrip('0')은 왼쪽의 0 삭제 001이면 1로 보여줌
            print("=")
            try:
                resultValue = eval(self.text_value.lstrip("0")) 
                self.le_view.setText(str(resultValue)) # la_view에 계산된 값을 출력
            except:
                self.le_view.setText("error")
        else: # 숫자 및 수식값이 눌려지면 self.text_value에 값을 더해나간다
            if btn_value == 'X':
                btn_value = '*' # x버튼이 눌리면 *으로 변경
            self.text_value = self.text_value + btn_value
            print(self.text_value)
            self.le_view.setText(self.text_value)


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()