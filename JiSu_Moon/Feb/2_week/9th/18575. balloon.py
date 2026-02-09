# 풍선팡 보너스 게임


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Min = 21e8
    Max = -21e8
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    for i in range(N):
        for j in range(N):
            Sum = arr[i][j]
            for x in range(4):
                for power in range(1, N):
                    dy = i+di[x]*power
                    dx = j+dj[x]*power
                    if dy<0 or dy>=N or dx<0 or dx>=N:
                        continue
                    Sum += arr[dy][dx]
            if Sum >= Max:
                Max = Sum
            if Sum < Min:
                Min = Sum
                          
    print(f'#{tc} {Max -Min}')    
            
