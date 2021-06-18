import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        mine = str(self.leMine.text())
        com = "";
        result = "";
        print(mine)
        
        import random as rd
        rand = rd.random()
        if(rand <= 0.33):
            com = "가위"
        elif(rand > 0.33 and rand <= 0.66):
            com = "바위"
        else:
            com = "보"
        print(com)
        
        self.leCom.setText(str(com))
            
        if(mine == com):
            result = "비김"
        elif(mine == "가위" and com == "보" or mine == "바위" and com == "가위" or mine == "보" and com == "바위"):
            result = "이김"
        else:
            result = "짐"
            
        self.leResult.setText(str(result))  
                
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    