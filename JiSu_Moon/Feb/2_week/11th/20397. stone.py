# 돌 뒤집기 게임 2


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    stone = list(map(int, input().split()))

    for z in range(M):
        i, j = map(int, input().split())

        for x in range(1, j+1):
            if 0<=i-1-x and i-1+x<N:
                if stone[i-1-x] == stone[i-1+x]:
                    if stone[i-1-x] == 1:
                        stone[i-1-x] = 0
                        stone[i-1+x] = 0
                    else:
                        stone[i-1-x] = 1
                        stone[i-1+x] = 1

    print(f'#{tc}', *stone)
