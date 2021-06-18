import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("myomok02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        
        
        super().__init__()
        self.setupUi(self)
        
        self.arr2D = [
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0],
            [0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0]
        ]
        
        self.pb2D = []
        self.flagWb = True
        self.flagOver = False
        for i in range(19):
            line = []
            for j in range(19):
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setGeometry(j * 40, i * 40, 40, 40)
                btn.setToolTip("{},{}".format(i,j))
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
        self.myrender()
        self.pbReset.clicked.connect(self.myReset)
        
    def myReset(self):
        self.flagWb = True
        self.flagOver = False
        
        for i in range(19):
            for j in range(19):
                self.arr2D[i][j] = 0
                
        self.myrender()
            
    def myclick(self):
        
        if(self.flagOver):
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        int_i = int(arr_ij[0])
        int_j = int(arr_ij[1])
        print(int_i, int_j)
       
        #if self.arr2D[int_i][int_j] > 0:
            #return
            
        stone = -1
        
        if(self.flagWb and self.arr2D[int_i][int_j] == 0):
            self.arr2D[int_i][int_j] = 1
            stone = 1
            
        elif(not self.flagWb and self.arr2D[int_i][int_j] == 0):
            self.arr2D[int_i][int_j] = 2
            stone = 2
            
        up = self.getUP(int_i,int_j,stone)
        dw = self.getDW(int_i,int_j,stone)
        ri = self.getRI(int_i,int_j,stone)
        le = self.getLE(int_i,int_j,stone)
        
        ur = self.getUR(int_i,int_j,stone)
        ul = self.getUL(int_i,int_j,stone)
        dr = self.getDR(int_i,int_j,stone)
        dl = self.getDL(int_i,int_j,stone)
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = le + ri + 1
        d4 = ul + dr + 1
        
        
        print("ri",ri)
        
        self.myrender()
        if(d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5):
            self.flagOver = True
            
            #QtWidgets.QMessageBox.information(self, "오목", "게임오버")
            if(self.flagWb):
                QtWidgets.QMessageBox.information(self, "오목", "백돌승리")
                
            else:
                QtWidgets.QMessageBox.information(self, "오목", "흑돌승리")
                
                
        self.flagWb = not self.flagWb
        
    def getUP(self,i,j,stone):
        cnt = 0
        
        try:
            while True:
                i -= 1
                if(i < 0):
                    return cnt
                if(self.arr2D[i][j] == stone):
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
            
    def getDW(self,i,j,stone):
        cnt = 0
        
        try:
            while True:
                i += 1
                if(i < 0):
                    return cnt
                if(self.arr2D[i][j] == stone):
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
        
    def getRI(self,i,j,stone):
        cnt = 0
        
        try:
            while True:
                j += 1
                if(i < 0):
                    return cnt
                if(j < 0):
                    return cnt
                if(self.arr2D[i][j] == stone):
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
       
    def getLE(self,i,j,stone):
        cnt = 0
        
        try:
            while True:
                j -= 1
                if(i < 0):
                    return cnt
                if(j < 0):
                    return cnt
                if(self.arr2D[i][j] == stone):
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt   
        
        
    def getUR(self,i,j,stone):
        cnt = 0
        
        try:
            while True:
                i -= 1
                j += 1
                if(i < 0):
                    return cnt
                if(j < 0):
                    return cnt
                if(self.arr2D[i][j] == stone):
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt  
        
    def getUL(self,i,j,stone):
        cnt = 0
        
        try:
            while True:
                i -= 1
                j -= 1
                if(i < 0):
                    return cnt
                if(j < 0):
                    return cnt
                if(self.arr2D[i][j] == stone):
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt  
        
    def getDR(self,i,j,stone):
        cnt = 0
        
        try:
            while True:
                i += 1
                j += 1
                if(i < 0):
                    return cnt
                if(j < 0):
                    return cnt
                if(self.arr2D[i][j] == stone):
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt  
        
    def getDL(self,i,j,stone):
        cnt = 0
        
        try:
            while True:
                i += 1
                j -= 1
                if(i < 0):
                    return cnt
                if(j < 0):
                    return cnt
                if(self.arr2D[i][j] == stone):
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt  
        
    def myrender(self):

        for i in range(19):
            for j in range(19):
                if(self.arr2D[i][j] == 0):
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                elif(self.arr2D[i][j] == 1):
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                else:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    