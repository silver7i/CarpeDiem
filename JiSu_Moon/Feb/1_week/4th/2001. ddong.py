# 파리퇴치


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = -21e8

    # 죽은 파리의 개수
    def Sum(i, j):
        Sum = 0
        for y in range(M):  # 파리채 영역
            for x in range(M):
                Sum += arr[y+i][x+j]
        return Sum

    # 죽은 파리의 최대값
    for i in range(N-M+1):  # 경우의 수
        for j in range(N-M+1):
            ret = Sum(i, j)
            if ret >= Max:
                Max = ret

    print(f'#{tc} {Max}')