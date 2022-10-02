class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack empty")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack Empty")

    def __len__(self):
        return len(self.items)


#? postfix
def postfix(str):
    li = ["*", "/", "+", "-"]
    s = Stack()
    s.push("_")
    t = ""

    for i in str:
        #* 만약 괄호에 들어가면 새로운 스택을 쌓음 (기준은 "_" <- 언더바)
        if i == "(": 
            s.push("_")
        elif i == ")":
            while s.top() != "_":
                t += s.pop()
            s.pop()
        else:
            if i not in li: 
                t += i
            elif s.top() in ["*", "/"]: 
                t += s.pop()

        if i in li:
            #* 만약 스택에 아무것도 없다면
            if s.top() == "_": 
                s.push(i)    

            #* 만약 스택에 무엇인가 있다면
            else:
                if s.top() in ["+", "-"]: 
                    s.push(i)
                else:
                    l = s.pop()
                    s.push(i)
                    s.push(l)

    #* 마지막인데 스택에 무엇인가 있다면 모두 출력
    while s.top() != "_":
        t += s.pop()
    s.pop()

    return t

#? infix
#! 632-4*+
def infix(str):
    s = Stack()
    li = ["*", "/", "+", "-"]
    
    for i in str:
        if i not in li:
            s.push(int(i))
        else:
            a = s.pop()
            b = s.pop()
            if i == "+":
                s.push(b + a)
            elif i == "-":
                s.push(b - a)
            elif i == "*":
                s.push(b * a)
            else:
                s.push(b / a)
    
    return s.pop()


a = postfix("6+(3-2+(6*5))*4")
print(a)
print(infix(a))
