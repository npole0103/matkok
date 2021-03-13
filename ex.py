import requests
import sys
from PyQt5.QtWidgets import *

#메인 윈도우 클래스 생성
class Mainwindow(QMainWindow):  
    def __init__(self):                           
        super().__init__()
        
        self.setWindowTitle("MatKok") # Title 설정
        self.resize(1024,800) #크기 설정 가로,세로 순
        
# GUI생성 및 루프생성
if __name__ == '__main__':
    app = QApplication(sys.argv) #루프생성
    mywindow = Mainwindow()
    mywindow.show()
    app.exec_()
