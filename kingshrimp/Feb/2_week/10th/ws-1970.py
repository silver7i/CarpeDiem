# ===
# 아이디어
# 탐욕 알고리즘
# 리스트에 잔돈을 큰것부터 넣고 앞에서부터 빼면 된다.
# 사실 이 문제 옛날에 풀어서 쉽게 풀었는데
# 잔돈 큰돈이 작은돈의 배수이기때문에 이렇게 쉽게 풀리는것이다.
# 배수가 아닐때는 다 브루트 포스 또는 DP로 풀어야한다.
# ===


import sys

sys.stdin = open('ws-1970i.txt')

# 잔돈 돌려주는 함수, 큰 잔돈부터 주기!
def solve(pay):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0] * 8
    for i in range(len(money)):
        change[i] = pay // money[i]
        pay = pay - change[i] * money[i]
    return change


T = int(input())

for tc in range(1, T+1):
    # 입력은 함수에서 받으면 안됨.
    pay = int(input())
    res = solve(pay)
    print(f'#{tc}')
    print(*res)