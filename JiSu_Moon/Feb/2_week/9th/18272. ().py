# 괄호검사


T = int(input())
for tc in range(1, T+1):
    txt = input()
    stack = []

    ans = 1
    for x in txt:
        if x == '(' or x == '{':  # 여는괄호 넣기
            stack.append(x)

        elif x == ')':
            if not stack or stack[-1] != '(':  # 스택이 비어있거나, 전에 여는괄호가 없다면
                ans = 0
                break
            stack.pop()  # 꺼내기

        elif x == '}':
            if not stack or stack[-1] != '{':  # 스택이 비어있거나, 전에 여는괄호가 없다면
                ans = 0
                break
            stack.pop()  # 꺼내기

    if stack:
        ans = 0

    print(f'#{tc} {ans}')