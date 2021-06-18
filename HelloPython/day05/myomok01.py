import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myqt01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        for i in range(10):
            self.btn = QPushButton('', self)
            self.btn.setIcon(QtGui.QIcon('0.png'))
            self.btn.setIconSize(QtCore.QSize(40,40))
            self.btn.setGeometry(i * 40, 0, 40, 40)
            self.btn.clicked.connect(self.myclick)
        
    def myclick(self):
        self.sender().setIcon(QtGui.QIcon('1.png'))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    