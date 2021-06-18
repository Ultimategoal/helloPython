import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myqt01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        
        for i in range(1, 362):
            for j in range(0, 721, 40):
                
                for k in range(0, 721, 40):
                    globals()['btn{}'.format(i)] = QPushButton('', self)
                    globals()['btn{}'.format(i)].setIcon(QtGui.QIcon('0.png'))
                    globals()['btn{}'.format(i)].setIconSize(QtCore.QSize(40,40))
                    globals()['btn{}'.format(i)].setGeometry(k, j, 40, 40)
                    
                
     
        #self.btn1 = QPushButton('', self)
        #self.btn1.setIcon(QtGui.QIcon('0.png'))
        #self.btn1.setIconSize(QtCore.QSize(40,40))
        #self.btn1.setGeometry(0, 0, 40, 40)
        
        #elf.btn10 = QPushButton('', self)
        #self.btn10.setIcon(QtGui.QIcon('0.png'))
        #self.btn10.setIconSize(QtCore.QSize(40,40))
        #self.btn10.setGeometry(360, 0, 40, 40)
        
        self.btn1.clicked.connect(self.myclick1)
        self.btn2.clicked.connect(self.myclick2)
        self.btn3.clicked.connect(self.myclick3)
        self.btn4.clicked.connect(self.myclick4)
        self.btn5.clicked.connect(self.myclick5)
        self.btn6.clicked.connect(self.myclick6)
        self.btn7.clicked.connect(self.myclick7)
        self.btn8.clicked.connect(self.myclick8)
        self.btn9.clicked.connect(self.myclick9)
        self.btn10.clicked.connect(self.myclick10)
        
    def myclick1(self):
        self.btn1.setIcon(QtGui.QIcon('1.png'))

    def myclick2(self):
        self.btn2.setIcon(QtGui.QIcon('1.png'))

    def myclick3(self):
        self.btn3.setIcon(QtGui.QIcon('1.png'))

    def myclick4(self):
        self.btn4.setIcon(QtGui.QIcon('1.png'))

    def myclick5(self):
        self.btn5.setIcon(QtGui.QIcon('1.png'))

    def myclick6(self):
        self.btn6.setIcon(QtGui.QIcon('1.png'))

    def myclick7(self):
        self.btn7.setIcon(QtGui.QIcon('1.png'))

    def myclick8(self):
        self.btn8.setIcon(QtGui.QIcon('1.png'))

    def myclick9(self):
        self.btn9.setIcon(QtGui.QIcon('1.png'))
        
    def myclick10(self):
        self.btn10.setIcon(QtGui.QIcon('1.png'))

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    