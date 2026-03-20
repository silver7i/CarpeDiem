# DFS
N = 5
M = 5
arr = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,0,0],
    [0,0,1,0,1],
    [0,1,0,0,1]
]

di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]
visited = [[0]*M for _ in range(N)]
cnt = 0

def dfs(y,x):
    visited[y][x] = 1
    for d in range(8):
        dy = y+di[d]
        dx = x+dj[d]
        if 0<=dy<N and 0<=dx<M:
            if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                dfs(dy,dx)
    
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            dfs(i,j)

print(cnt)