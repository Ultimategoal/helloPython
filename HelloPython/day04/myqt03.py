import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myqt03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        num1 = str(self.le1.text())
        num1 = int(num1)
        num2 = str(self.le2.text())
        num2 = int(num2)
        print(num1 + num2)
        num3 = num1 + num2
        self.le3.setText(str(num3))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    