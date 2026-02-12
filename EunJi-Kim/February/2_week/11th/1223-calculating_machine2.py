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

    icp = {'*':2, '+': 1} # stack 밖에 있을 때 우선 순위 (클수록 높음)

    stack = []      # 후위 표기식 만들 때는 연산자 stack / 계산할 때는 정수 stack
    postfix = ''    # 후위연산 결과값

    for token in arr:
        if token not in icp: # * + 연산자가 아니면
            postfix += token
        else:     # 연산자면 / 스택에 넣을 건데 우선순위 따져가면서
            if not stack or icp[token] > icp[stack[-1]]: # 만약 스택이 비어져있거나, 새로 들어올 연산자 우선순위가 높은 경우
                stack.append(token)
            elif icp[token] <= icp[stack[-1]]: # 새로 들어올 값이 우선순위가 낮거나 같으면
                while stack and icp[token] <= icp[stack[-1]]: # stack 비워지기 전, 토큰 우선순위가 낮다면 계속 돌면서
                    postfix += stack.pop()
                # 토큰 우선순위가 높을 때 stack에 넣고 멈추기
                stack.append(token)

    while stack:
        postfix += stack.pop()

    for token in postfix:
        if token not in icp:    # 연산자가 아닌 정수면 stack에 넣음
            stack.append(int(token))
        else:   # 연산자면
            op2 = stack.pop()
            op1 = stack.pop()
            if token == '*':
                stack.append(op1 * op2)
            elif token == '+':
                stack.append(op1 + op2)
    
    print(f'#{test_case} {stack.pop()}')

    