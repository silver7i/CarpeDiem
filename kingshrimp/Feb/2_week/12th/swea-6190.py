import sys

sys.stdin = open('swea-2805i.txt')

def is_increase(n):

    last_digit = n % 10  # 현재 가장 오른쪽에 있는 자릿수
    num = n // 10  # 마지막 자리를 제외한 나머지 숫자

    while num > 0:
        current_digit = num % 10  # 그 다음 자리 숫자

        # 앞자리(current)가 뒷자리(last)보다 크면 단조 증가가 아님
        if current_digit > last_digit:
            return False

        # 비교 대상을 갱신하고 숫자를 줄임
        last_digit = current_digit
        num //= 10

    return True


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    # -1을 넣는거를 한다면 굳이 False를 안넣어도 된다.
    max_value = -1

    for i in range(N):
        for j in range(i + 1, N):
            mul_res = array[i] * array[j]
            # 2. 단조 증가 함수를 for문에 넣는 방식.... ai한테 배웠다...
            # for문 안에 함수를 써야한다는 관념에서 벗어나자..
            if is_increase(mul_res):
                # 3. 최댓값 갱신
                if mul_res > max_value:
                    max_value = mul_res

        print(f"#{tc} {res}")





