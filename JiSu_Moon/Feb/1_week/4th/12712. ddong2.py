# 파리퇴치3


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max_1 = -21e8
    Max_2 = -21e8

    # 기준 좌표
    for y in range(N):
        for x in range(N):

            # + 형태
            di_1 = [-1, 1, 0, 0]
            dj_1 = [0, 0, -1, 1]
            Sum_1 = arr[y][x]
            for d in range(4):
                for power in range(1, M):
                    dy = y+di_1[d]*power
                    dx = x+dj_1[d]*power
                    if dy >= N or dy < 0 or dx >= N or dx < 0:
                        continue
                    Sum_1 += arr[dy][dx]
                if Sum_1 > Max_1:
                    Max_1 = Sum_1

            # x 형태
            di_2 = [-1, 1, 1, -1]
            dj_2 = [1, 1, -1, -1]
            Sum_2 = arr[y][x]
            for d in range(4):
                for power in range(1, M):
                    dy = y + di_2[d] * power
                    dx = x + dj_2[d] * power
                    if dy >= N or dy < 0 or dx >= N or dx < 0:
                        continue
                    Sum_2 += arr[dy][dx]
                if Sum_2 > Max_2:
                    Max_2 = Sum_2

            if Max_2 > Max_1:
                result = Max_2
            else:
                result = Max_1


    print(f'#{tc} {result}')