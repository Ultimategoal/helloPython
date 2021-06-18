import random as rd
a = input("홀/짝중에 선택하시오")
b = ["홀", "짝"]

c = rd.choice(b)

if(a == c):
    print("정답입니다.")
else:
    print("틀렸습니다.")

print("-----------------------------------------")

mine = input("홀/짝 중에 선택하시오")
    
com = ""

rnd = rd.random()

if(rnd > 0.5):
    com = "홀"
else:
    com = "짝"

if com == mine:
    result = "이김"
else:
    result = "짐"

print("mine:",mine)
print("com:",com)
print("result:",result)