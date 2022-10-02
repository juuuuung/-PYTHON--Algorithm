def Fibo(n, f1, total):
    if n > 1:
        print(n, f1, total)
        return Fibo(n-1, total, total+f1)
    else:
        return total

print(Fibo(int(input()), 0, 1))