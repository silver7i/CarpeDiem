def check_parentheses(bracket_str):
    '''
    괄호 문자열 bracket_str을 입력받아,
    모든 '('와 ')'의 짝이 올바른지 검사한다.
    짝이 맞으면 1, 아니면 -1을 반환한다.
    '''
    stack = []
    # 기본값을 1로 설정(짝이 맞는 상태),
    # 중간에 틀림이 발견되면 -1로 바꾸고 종료
    result = 1

    for char in bracket_str:
        # 여는 괄호 '('는 스택에 push
        if char == '(':
            stack.append(char)
        # 닫는 괄호 ')'를 만나면, 스택에서 pop
        elif char == ')':
            # 스택이 비어있다면 짝이 안 맞음(underflow)
            # if not stack:
            if len(stack) == 0:
                result = -1
                return result
            # 스택에서 여는 괄호를 pop
            stack.pop()

        # 그 외 문자는 무시하거나 별도 로직 처리 가능
        # (문제 요구사항에 따라 달라질 수 있음)

    # 모든 반복 후 스택이 남아 있으면 짝이 완벽하지 않음
    # if stack:
    if len(stack) != 0:
        result = -1

    return result


# ----------------------------
import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    bracket_line = input().strip()  # 괄호 문자열
    answer = check_parentheses(bracket_line)
    print(f'#{tc} {answer}')
