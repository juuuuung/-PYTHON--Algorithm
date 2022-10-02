import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

count = 0

for i in arr:
    if i == 1:
        continue
    
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt+= 1

    if cnt == 1:
        count+=1

print(count)