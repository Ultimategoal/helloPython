from matplotlib.pyplot import plot
a = int(input("첫 번째 수를 입력하세요"))
b = int(input("두 번쨰 수를 입력하세요"))
sum = 0
for i in range(a,b+1):
    sum += i
print(sum)