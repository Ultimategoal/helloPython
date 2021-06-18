sum = 0

for i in range(1, 1001):
    if(i % 3 == 0):
        continue
    sum += i
    
print(sum)