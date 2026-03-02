# 미로의 거리


from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    def bfs(y,x):
        q = deque()
        q.append((y,x,-1))
        visited[y][x] = 1

        while q:
            nowy, nowx, size = q.popleft()
            size += 1
            for d in range(4):
                dy = nowy+di[d]
                dx = nowx+dj[d]
                if 0<=dy<N and 0<=dx<N:
                    if arr[dy][dx] == 0 and visited[dy][dx] == 0:
                        visited[dy][dx] = 1
                        q.append((dy,dx,size))
                    elif arr[dy][dx] == 3:                    
                        return size             
        return 0


    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                result = bfs(i,j)
            
    print(f'#{tc} {result}')