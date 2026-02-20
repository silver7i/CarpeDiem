import sys
from pathlib import Path

file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)

sys.stdin = open(file_path, "r")

##############################

def check(arr):
    stack = []
    for token in arr:
        if token in "[{(<":
            stack.append(token)
        elif token == ']':
            if not stack or stack.pop() != '[':
                return 0
        elif token == '}':
            if not stack or stack.pop() != '{':
                return 0
        elif token == ')':
            if not stack or stack.pop() != '(':
                return 0
        elif token == '>':
            if not stack or stack.pop() != '<':
                return 0
    return 1


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = input()

    print(f'#{tc}', check(arr))

