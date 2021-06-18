import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myqt01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.state = 0
        self.btn1 = QPushButton('', self)
        self.btn1.setIcon(QtGui.QIcon('0.png'))
        self.btn1.setIconSize(QtCore.QSize(40,40))
        self.btn1.setGeometry(0, 0, 40, 40)
        self.btn1.clicked.connect(self.myclick)
        
    def myclick(self):
        self.state += 1
        int_mode = self.state % 3
        self.btn1.setIcon(QtGui.QIcon('{}.png'.format(int_mode)))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    