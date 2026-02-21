import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True) 

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

T = int(input())
for test_case in range(1, T+1):
    arr = input()

    result = 1
    stack = []
    for i in arr:
        if i in "{(":
            stack.append(i)
        elif i == ")":
            if not stack or stack.pop() != '(':
                result = 0
                break
        elif i == "}":
            if not stack or stack.pop() != "{":
                result = 0
                break

    if stack:
        result = 0

    print(f'#{test_case} {result}')
