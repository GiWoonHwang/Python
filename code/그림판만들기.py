import sys 
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


ui_path = r".\그림판.ui"
form_class = uic.loadUiType(ui_path)[0] 


class WindowClass(QMainWindow, form_class) : 
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.brushColor = Qt.black  

        # lb_canvas를 canvas로 설정합니다
        self.canvas = QtGui.QPixmap(self.lb_canvas.width(), self.lb_canvas.height()) 
        self.canvas.fill(QtGui.QColor("white"))  
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.clicked.connect(self.btn_clicked) # 검정설정
        self.btn_black.setStyleSheet('background:black')

        self.btn_red.clicked.connect(self.btn_clicked) # 빨강설정
        self.btn_red.setStyleSheet('background:red')

        self.btn_blue.clicked.connect(self.btn_clicked) # 파랑설정
        self.btn_blue.setStyleSheet('background:blue')

        # self.btn_green.clicked.connect(self.btn_clicked) # 녹색은 나중에 내가 따로 만들자
        # self.btn_green.setStyleSheet('background:green')
        
        
        self.btn_clear.clicked.connect(self.btn_clear_clicked) 
    
    def btn_clicked(self):
        btn_value = self.sender().objectName()
        print(btn_value)
        if btn_value == 'btn_black':
            self.brushColor = Qt.black
        elif btn_value == 'btn_red':
            self.brushColor = Qt.red
        elif btn_value == 'btn_blue':
            self.brushColor = Qt.blue
        # elif btn_value == 'btn_green':
        #     self.brushColor = Qt.green
           
    def btn_clear_clicked(self): # 흰색으로 채워 지워진것처럼 보임
        print("모두지움")
        self.canvas.fill(QtGui.QColor("white"))
        self.lb_canvas.setPixmap(self.canvas)

    def mouseMoveEvent(self, e): # 마우스를 클릭하여 이동시 이동좌표 출력
        painter = QtGui.QPainter(self.lb_canvas.pixmap())
        painter.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap)) 
        painter.drawPoint(e.x(), e.y())
        painter.end()
        self.update()

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_()