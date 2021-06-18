import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        num1 = str(self.leMine.text())
        num2 = "";
        result = "";
        print(num1)
        
        import random as rd
        rand = rd.random()
        if(rand <= 0.5):
            num2 = "홀"
        else:
            num2 = "짝"
        print(num2)
        
        self.leCom.setText(str(num2))
            
        if(num1 == num2):
            result = "이김"
        else:
            result = "짐"
            
        self.leResult.setText(str(result))  
                
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    