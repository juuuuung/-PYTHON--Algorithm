m = int(input())
n = int(input())

result = 0
min = 0

for i in range(m, n+1):
    count = 0
    if i == 1:
        continue
    for j in range(2, round(i**(1/2))+1):
        if count == 2:
            break
        if i % j == 0:
            count += 2

    if count == 0:
        result += i
        if min == 0:
            min = i
    
if min == 0:
    print(-1)
else:
    print(result, min)