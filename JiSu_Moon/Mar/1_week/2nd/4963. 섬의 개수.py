from collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: 
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    di = [-1,-1,-1,0,0,1,1,1]
    dj = [-1,0,1,-1,1,-1,0,1]
    cnt = 0

    def bfs(y, x):
        q = deque()
        q.append((y,x))
        visited[y][x] = 1

        while q:
            nowy, nowx = q.popleft()
            for d in range(8):
                dy = nowy+di[d]
                dx = nowx+dj[d]
                if 0<=dy<h and 0<=dx<w:
                    if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                        visited[dy][dx] = 1
                        q.append((dy,dx))


    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                bfs(i,j)

    print(cnt)