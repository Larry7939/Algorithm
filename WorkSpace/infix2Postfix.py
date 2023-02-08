class Stack:
    def __init__(self):
        self.top= []
    def isEmpty(self)->bool:
        return len(self.top)==0
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def size(self):
        return len(self.top)
    def clear(self):
        self.top = []
    def __str__(self):
        return str(self.top)

def evalPostfix(expr):
#후위 표기법으로 되어있는 문자열을 계산하는 함수
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if token=='+':
                s.push(val1+val2)
            elif token=='-':
                s.push(val1-val2)
            elif token=='*':
                s.push(val1*val2)
            elif token=='/':
                s.push(val1/val2)
        else:
            s.push(float(token))
    return s.pop()
def precedence(op):
    if op=="("or op==")": return 0
    elif op=='+'or op=='-': return 1
    elif op=='*' or op=='/': return 2
    else: return -1
def infix2Postfix(expr):   #1/2*4*(1/4)
    s = Stack()
    output = []
    #expr은 중위표기 수식임.
    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op=='(':break
                else:
                    output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                #만약, 최근에 넣은 연산자의 우선순위가 더 높다면, output에 op를 추가한다.
                #기존에 있는 걸 먼저 연산해버리는 거임.
                 #기존의 스택에 우선순위가 더 높은 애가 있으면,
                #걔들을 우선적으로 출력하고 pop한다.
                #그 후에 term을 while문 밖에서 push한다.
                if(precedence(term)<=precedence(op)):
                    output.append(op)
                #더 높은 기존의 연산자를 출력하고, 이미 출력했으니 pop()한다.
                    s.pop()
                #만약에 새로들어온 term이 제일 크면? 그냥 break해서 while문 밖에서 push한다.
                else: break
            #연산자 term을 스택에 push한다. 
            s.push(term)
        #앞에서 전부 비교해 보고, 괄호나 연산자가 아니면 출력한다.(숫자)
        else:
            output.append(term)
    #스택이 비어있지 않은 동안, 계속 append한다.
    while not s.isEmpty():
        output.append(s.pop())
    return output
infix = input("중위표기 수식을 입력하세요.: ")
postfix = infix2Postfix(infix)
print("후위 표기식",postfix)
#후위 표기법으로 전환 후 계산
result = evalPostfix(postfix)
print("결과값 :",result)