import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

#메인 윈도우 클래스 생성
class Mainwindow(QMainWindow):  
    def __init__(self, parent=None):           
        super(Mainwindow,self).__init__(parent)

        self.initUi()
        self.center()

        ##### 위젯클래스 메인윈도우의 센터에 셋팅
        self.mywidget = Widgets(self)
        self.setCentralWidget(self.mywidget)

    # 초기 UI
    def initUi(self):
        self.setWindowTitle("MatKok") # Title 설정
        self.setWindowIcon(QIcon("메인아이콘.png"))
        self.resize(1280,720) #크기 설정 가로,세로 순

        ##### 상태표시줄 생성
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        ##### 타이머 설정 - 상태표시줄 현재시간
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)
        
        ##### 메뉴바 설정        
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)        

        menubar.addMenu('&Edit')
        menubar.addMenu('&View')
        menubar.addMenu('&Tools')
        menubar.addMenu('&Help')

        ##### 툴바 설정
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.triggered.connect(qApp.quit)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)


    ##### 상태표시줄에 들어갈 현재시간
    def timeout(self):
        current_time = QTime.currentTime()
        text_time = current_time.toString("hh:mm:ss")
        time_msg = "현재시간 : " + text_time

        self.statusbar.showMessage(time_msg)

    # 화면 위치 중앙
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())   
    
    def closeEvent(self, QCloseEvent):
        re = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?",
                    QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

##### 위젯 영역
class Widgets(QWidget):
    def __init__(self, parent):           
        super(Widgets,self).__init__(parent)

        ##### 위젯 함수 실행
        self.initWidget()

    ##### 위젯셋팅
    def initWidget(self):
        ##절대적 레이아웃
        label = QLabel("라벨", self)
        label.move(40, 25)        
        combo = QComboBox(self)
        combo.move(80, 20)

        



# GUI생성 및 루프생성
if __name__ == '__main__':
    app = QApplication(sys.argv) #루프생성
    mywindow = Mainwindow()
    mywindow.show()
    app.exec_()
