t = int(input())

for tc in range(1, t+1):
    forth = input().split()
    
    # 숫자는 스택에 넣는다.
    # 연산자를 만나면 숫자 두개를 꺼내 연산하고 결과를 다시 스택에 넣는다
    # . 스택에서 숫자를 꺼내 출력한다.
    stack = []

    for item in forth:
        if item == '+':
            if not stack:
                answer = "error"
                break
            num1 = int(stack.pop())
            if not stack:
                answer = "error"
                break
            num2 = int(stack.pop())
            result = num2 + num1
            stack.append(result)
            
        elif item == '-':
            if not stack:
                answer = "error"
                break
            num1 = int(stack.pop())
            if not stack:
                answer = "error"
                break
            num2 = int(stack.pop())
            result = num2 - num1      
            stack.append(result)    
            
        elif item == '*':
            if not stack:
                answer = "error"
                break
            num1 = int(stack.pop())
            if not stack:
                answer = "error"
                break
            num2 = int(stack.pop())
            result = num2 * num1     
            stack.append(result)

        elif item == '/':
            if not stack:
                answer = "error"
                break
            num1 = int(stack.pop())
            if not stack:
                answer = "error"
                break
            num2 = int(stack.pop())
            result = int(num2 / num1)
            stack.append(result)    

        elif item in '.':
            if len(stack) == 1:
                answer = stack.pop()
            else:
                answer = "error"
            break

        else:
            stack.append(int(item))

    print(f"#{tc} {answer}")