n = int(input())
i = 2
r = int(n**0.5)

# r = 3, i = 2
while i <= r:
    # n % i = 10 % 2 = 0
    while not n% i:
        # 2
        print(i)
        # n//= i  =>  5
        n //= i
    i += 1
if n > 1:
    print(n)