# ---
# 이게 왜 스택이지???
# ---

import sys

sys.stdin = open('ws-04i.txt')

def solve(string):
    stack = []

    for char in string:
        if len(stack) == 0 or char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()

    return len(stack)

T = int(input())

for tc in range(1, T+1):
    string = input()

    print(solve(string))

# for tc in range(1, T+1):
#     char = input()
#     for i in char:
#         if char[i] == char[i+1]
#             char.remove(char[i])