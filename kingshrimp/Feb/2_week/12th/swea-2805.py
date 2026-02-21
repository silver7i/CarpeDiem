import sys

sys.stdin = open('swea-2805i.txt')

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    # range의 시작점 끝점 지정
    m = N // 2
    n = N // 2
    total_profit = 0
    for i in range(N):
        total_profit += sum(matrix[i][m: n + 1])
        if i < N // 2:
            m -= 1
            n += 1
        else:
            m += 1
            n -= 1

    print(f"#{tc} {total_profit}")



