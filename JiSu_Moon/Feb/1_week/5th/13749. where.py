# 어디에 단어가 들어갈 수 있을까


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0


    # 가로 탐색
    for i in range(N):
        count = 0
        for j in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == K:
                    total += 1
                count = 0
        if count == K:
            total += 1

    # 세로 탐색
    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                if count == K:
                    total += 1
                count = 0
        if count == K:
            total += 1


    print(f'#{tc} {total}')