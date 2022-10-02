N = int(input())

a = N // 5
b = N % 5
cnt = 0

while a >= 0:
    if b % 3 == 0:
        cnt = a +(b // 3)
        break
    a -= 1
    b += 5

if cnt > 0:
    print(cnt)
else:
    print(-1)