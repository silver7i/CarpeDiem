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

    stack = [0] * (N // 2)
    top = -1
    postfix = ''

    icp = {'(':3, '*':2, '+':1}    # 밖에 있을 때의 우선 순위(클수록 높음) 
    isp = {'(':0, '*':2, '+':1}    # 스택 안에 있을 때의 우선 순위

    # 후위표현식으로 바꾸기
    for token in arr:
        if token not in '(*+)':    # 연산식이 아니면/정수면
            postfix += token
        elif token == ')':      # 닫는 괄호가 나오면 여는괄호가 나올때까지 while
            while top > -1 and stack[top] != '(':
                postfix += stack[top]
                top -= 1
            if top != -1:       # 맨 끝의 괄호가 아니면 여는괄호 버림
                top -= 1
        else:                   # 연산식이면
            if top == -1 or icp[token] > isp[stack[top]]:
                top += 1
                stack[top] = token
            elif top > -1 and icp[token] <= isp[stack[top]]:
                while top > -1 and icp[token] <= isp[stack[top]]:
                    postfix += stack[top]
                    top -= 1
                top += 1        
                stack[top] = token


    # 계산하기
    stack = [0] * (N // 2)
    top = -1

    for token in postfix:
        if token not in '*+': # 정수면 stack에 넣기
            top += 1
            stack[top] = int(token)
        else:
            right = stack[top]
            top -= 1
            left = stack[top]
            top -= 1
            if token == '*':
                top += 1
                stack[top] = left * right
            elif token == '+':
                top += 1
                stack[top] = left + right


    print(f'#{test_case}', stack[top])
    