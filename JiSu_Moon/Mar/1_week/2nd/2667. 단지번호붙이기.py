from collections import deque
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]
visited = [[0]*N for _ in range(N)]
apt = []

def bfs(x, y):
    global visited
    q = deque()
    q.append((x, y))
    size = 0

    while q:
        nowx, nowy = q.popleft()
        size += 1
        for d in range(4):
            dx = nowx+di[d]
            dy = nowy+dj[d]
            if 0<=dx<N and 0<=dy<N:
                if arr[dx][dy] == 1 and visited[dx][dy] == 0:
                    visited[dx][dy] = 1
                    q.append((dx, dy))
    return size

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
             
            apt.append(bfs(i, j))

apt.sort()
print(len(apt))
for x in apt:
    print(x)