a = int(input("첫 수를 입력하세요!"))
b = int(input("두 번째 수를 입력하세요"))

def plus(a,b):
    if(a < b):
        return a+b
    else:
        return b+a


sum = plus(a,b)
print(sum)