def trans(tc):
    stack = []
    icp = {'(':3, '*':2, '+':1}
    isp = {'(':0, '*':2, '+':1}

    susik = ''

    for x in tc:
        # 피연산자
        if x not in '(+*)':
            susik += x
        
        # ) 닫는 괄호일 때 스택이 ( 여는 괄호 일때까지 팝~
        elif x == ')':
            while stack[-1] != '(':
                susik += stack[-1]
                stack.pop()
            stack.pop() # 여괄도 버려
        else: # x in '(+-*/'
            # 토큰 우선순위가 더 높을 때, 빈스택일때 푸쉬해~
            if not stack or icp[x] > isp[stack[-1]]:
                stack.append(x) 
            
            # 토큰 우선순위가 더 작거나 같을 때, 더 커질 때 까지 팝해~ 커지면 푸쉬해 ~
            elif icp[x] <= isp[stack[-1]]:
                while stack and icp[x] <= isp[stack[-1]]:
                    susik += stack[-1]
                    stack.pop()
                stack.append(x)

    return susik

def trans_calculator(susik):
    # 숫자는 스택에 넣는다.
    # 연산자를 만나면 숫자 두개를 꺼내 연산하고 결과를 다시 스택에 넣는다
    # . 스택에서 숫자를 꺼내 출력한다.
    stack = []

    for item in susik:
        if item == '+':
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            result = num2 + num1
            stack.append(result)
                
        elif item == '*':
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            result = num2 * num1     
            stack.append(result)
        
        else:
            stack.append(int(item))
    
    return stack[0]

for tc_num in range(1, 11):
    n = int(input()) # tc길이
    tc = input()

    print(f"#{tc_num} {trans_calculator(trans(tc))}")