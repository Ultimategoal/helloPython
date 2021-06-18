import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        num = str(self.le.text())
        num = int(num)
        result = "" 
        
        for i in range(1, 10):
            result += str(num) + "*" + str(i) + " = " + str(num*i) + "\n"
            self.te.setText(result)
        
            
                
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()