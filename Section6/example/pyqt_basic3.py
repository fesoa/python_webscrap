import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore

class TestForm(QMainWindow): # QtWidgets에서 상속받아옴
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("PyQT Test")
        self.setGeometry(800,400,800,500)

        label_1 = QLabel("입력테스트", self)
        label_2 = QLabel("출력테스트", self)

        label_1.move(20,20)
        label_2.move(20,60)

        self.lineEdit = QLineEdit("", self) # default 값
        self.plainEdit = QtWidgets.QPlainTextEdit(self)

        self.lineEdit.move(200, 20)
        self.plainEdit.setGeometry(QtCore.QRect(20,90,361,231))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestForm()
    window.show()

    app.exec_()
