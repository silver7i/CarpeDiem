T = int(input())

for tc in range(1, T + 1):
    # list() 없이 바로 문자열로 받음
    check_str = input() 

    stack = []

    # idx 없이 문자열에서 바로 한 글자씩 꺼내기
    for char in check_str:
        # 스택이 비어있으면 무조건 넣기
        if not stack:
            stack.append(char)
        # 스택이 비어있지 않고, 맨 위 글자가 현재 글자와 같다면? -> 팡! (제거)
        elif stack[-1] == char:
            stack.pop()
        # 맨 위 글자와 다르다면? -> 쌓기
        else:
            stack.append(char)

    # 빈 리스트의 len()은 0이므로, 조건문 없이 바로 출력 가능
    print(f"#{tc} {len(stack)}")