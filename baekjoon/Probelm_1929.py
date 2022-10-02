def prime(s, e):
    arr = [False, False] + [True] * (e + 1)
    t = int(e ** 0.5)+1
    for i in range(2, t):
        if arr[i]:
            for j in range(i+i, e, i):
                arr[j] = False
    return [n for n in range(s, e) if arr[n]]

s, e = map(int, input().split())
for i in prime(s,e):
    print(i)