import sys

def fac(n, total):
    for i in range(1, n):
        total *= i
    return print(total)

N = int(sys.stdin.readline())+1

fac(N, 1)