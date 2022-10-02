import sys

def prime(s, e):
    arr = [False, False] + [True] * (e + 1)

    for i in range(2, int(e ** 0.5)+1):
        if arr[i]:
            for j in range(i + i, e+1, i):
                arr[j] = False
    return print(len([n for n in range(s+1,e+1) if arr[n]]))


while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    prime(n, n*2)