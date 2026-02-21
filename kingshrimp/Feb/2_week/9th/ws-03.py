# ---
# 1. 아이디어
# 1-1. 리스트를 통한 괄호 넣기
# 1-2. 딕셔너리를 활용한 넣기
# 2. 리스트를 통해 풀기
#


# ---
import sys

# sys.stdin = open('ws-03i.txt')

T = int(input())

for tc in range(1, T + 1):
    char = input()
    error = 1
    stack = []

    for i in char:
        if i == '(' or i == '{':
            stack.append(i)

        elif i == ')':
            if not stack or stack.pop() != '(':
                error = 0
                break
        elif i == '}':
            if not stack or stack.pop() != '{':
                error = 0
                break

    if stack:
        error = 0

    print(f'#{tc} {error}')




# import sys
#
# sys.stdin = open('ws-03i.txt')
#
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     char = input()
#     error = 1
#     stack = [0] * 2
#
#     for i in char:
#         if i == '(':
#             stack[0] += 1
#         elif i == '{':
#             stack[1] += 1
#         elif i == ')':
#             if stack[0] == 0:
#                 error = 0
#                 break
#             stack[0] -= 1
#         elif i == '}':
#             stack[1] -= 1
#
#     if stack[0] != 0 or stack[1] != 0:
#         error = 0
#
#
#
#     print(f'#{tc} {error}')

