def is_prime(n):
    global bool
    #n = 4 => 3개 추가 n-1개
    if len(bool) < n+1:
        bool += [True] * ((n+1) - len(bool))

        for i in range(2, int(n ** 0.5)+1):
            if bool[i]:
                for j in range(i+i, n+1, i):
                    bool[j] = False
    else:
        if bool[n]:
            return True
        else:
            return False

def mk(n):    
    first = n // 2    
    two = n - first    
    while True:
        prime_first = is_prime(first)
        prime_two = is_prime(two)
        #둘중 하나가 False 라면 실행
        if prime_first == False or prime_two == False:
            first -= 1
            two += 1
        # 둘중 하나가 true 라면 실행
        elif prime_first == True and prime_two == True:
            return print(first, two)

       
import sys 
bool = [False, False]
t = int(input()) 
arr = [int(sys.stdin.readline()) for _ in range(t)]
for i in arr:    
    mk(i)