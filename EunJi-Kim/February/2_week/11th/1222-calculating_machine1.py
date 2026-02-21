import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

T = 10
for test_case in range(1, T+1):  
    N = int(input())
    arr = input()

    stack = [] # 후위 표기식 만들 때는 연산자 stack / 계산할 때는 정수 stack
    postfix = ''

    # 후위 표현식 만들기
    for token in arr:
        if token != '+':    # 정수면 결과물에 더하고
            postfix += token   
        else:       # 연산자면
            while stack:    # 어차피 한번만 돌거 같지만 일단 스택이 있는 동안
                postfix += stack.pop()
            stack.append(token)

    while stack:
        postfix += stack.pop()

    # 후위 표현식 더하기
    for token in postfix:
        if token != '+':
            stack.append(int(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1 + op2)

    print(f'#{test_case} {stack.pop()}')