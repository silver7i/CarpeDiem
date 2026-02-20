import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

T = int(input())
for test_case in range(1, T+1):
    arr = list(input().split())
    
    stack = []  # 연산자 계산하기 위한 도구
    result = 0

    for token in arr:
        if token not in '*/+-.':    # 연산자가 아니면
            stack.append(int(token))
        elif token == '.':  # . 을 만나면
            if len(stack) > 1:    # 스택 길이가 1이 아니면 최종 연산 이외의 결과가 추가로 들어왔을 수 있음
                result = 'error'
            else:
                result = stack.pop()    
            
        else:   # 연산자면
            if len(stack) <= 1:
                result = 'error'
                break

            op2 = stack.pop()
            op1 = stack.pop()
            if token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                stack.append(op1 // op2)
            elif token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)

    print(f'#{test_case} {result}')
        