# ===

# ===

import sys

sys.stdin = open('swea-4874i.txt')

def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token == '.':
            if len(stack) == 1:
                return stack.pop()
            else:
                return 'error'

            # 2. 숫자인 경우: 스택에 추가
        elif token.isdigit():
            stack.append(int(token))
        # 1. 피연산자(숫자)인 경우: 스택에 push
            if token.isdigit():
                stack.append(int(token))  # 계산을 위해 정수형 변환 필수

            # 2. 연산자인 경우: 스택에서 2개 꺼내서 계산
            else:
                # [중요] 스택은 LIFO이므로, 먼저 꺼낸 것이 '오른쪽' 피연산자임
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    # 나눗셈은 정수 나눗셈(//) 혹은 실수 나눗셈(/) 상황에 맞춰 사용
                    stack.append(int(left / right))

    # 3. 최종 결과 반환
    return stack.pop()


# T = 10 (문제에 주어진 대로 케이스 수 설정)
T = int(input())

for tc in range(1, T + 1):
    # map(int, ...)를 절대 쓰지 마세요! 연산자가 포함되어 있으니까요.
    statement = input().split()

    res = evaluate_postfix(statement)
    print(f'#{tc} {res}')




