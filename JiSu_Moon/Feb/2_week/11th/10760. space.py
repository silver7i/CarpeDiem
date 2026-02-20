#  우주선착륙2


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input(). split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):

            di = [-1,-1,-1,0,1,1,1,0]
            dj = [-1,0,1,1,1,0,-1,-1]
            count = 0
            for d in range(8):
                dy = i+di[d]
                dx = j+dj[d]
                if 0<=dy<N and 0<=dx<M:
                    if arr[dy][dx] < arr[i][j]:
                        count += 1
            if count >= 4:
                cnt += 1

    print(f'#{tc} {cnt}')