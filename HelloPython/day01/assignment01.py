import random as rd

mine = input("가위 바위 보 중에 하나를 선택하시오")

a = rd.random()

com = ""

if(a <= 0.33):
    com = "가위"
elif a > 0.33 and a <= 0.66:
    com = "바위"    
else:
    com = "보"
    
if(mine == com):
    result = "비김"
elif(mine == "가위" and com == "바위" or mine== "바위" and com == "보" or mine== "보" and com == "가위"):
    result = "짐"
else:
    result = "이김"
    
print("mine:",mine)
print("com:",com) 
print("result:",result)