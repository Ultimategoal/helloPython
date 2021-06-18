a = int(input("첫 번쨰 범위 입력"))
b = int(input("두 번째 범위 입력"))
c = int(input("배수를 입력하세요"))
sum = 0
for i in range(a,b):
    if(i % c == 0):
       sum += i
       
print(sum) 