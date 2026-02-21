t = int(input())

for tc in range(1, t+1):
    csl = list(input()) # check_str_list == csl

    # 출력 -> 반복문자 지운 후 남은 문자열의 길이. 남은 문자열이 없으면 0을 출력.
    ## 스택으로 푸는 거겠지
    stack = []
    for _ in range(len(csl)): # csl 남은 길이만큼만 수행하면되니까
        # 빈스택이면 푸쉬하면 됨
        if not stack:
            stack.append(csl[-1]) # stack = B # stack = A
            csl.pop()

        # 만약 스택 마지막 이랑 csl 마지막이랑 같으면 스택 팝하면됨
        elif stack[-1] == csl[-1]:
            stack.pop() # stack = B # stack = []
            csl.pop()

        # 만약 스택 마지막이랑 csl 마지막이랑 다르면 스택에 푸쉬하면됨
        elif stack[-1] != csl[-1]:
            stack.append(csl[-1]) # stack = B, C
            csl.pop()


    if not stack:
        answer = 0
    else:
        answer = len(stack)

    print(f"#{tc} {answer}")