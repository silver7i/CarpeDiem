import sys

sys.stdin = open('ws-05i.txt')


# 이니 인풋 이렇게 통일성 없게 주면 속상하지
T = 10

for tc in range(1, T + 1):
    N, M = input().split()

    stack = []

    for char in M:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    result = "".join(stack)
    print(f"#{tc} {result}")