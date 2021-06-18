import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from Cython.Compiler.Naming import self_cname
from PyQt5 import QtCore, QtWidgets

form_class = uic.loadUiType("myqt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        self.pbCall.clicked.connect(self.myclickCall)
      
        
    def myclick(self):
        str_old = self.le.text()
        str_new = self.sender().text()
        print(str_old)
        print(str_new)
        self.le.setText(str_old+str_new)
        
    def myclickCall(self):
        str_tel = self.le.text()
        QtWidgets.QMessageBox.information(self, "calling", str_tel)
            
                
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()