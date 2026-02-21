dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def trail(y, x):
    # 저장한 값 그대로 쓸거야
    if dp[y][x] != 0:
        return dp[y][x]
    
    # 초기값 설정
    cur_h = graph[y][x]
    min_h = cur_h
    next_y, next_x = -1, -1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if cur_h > graph[ny][nx]:
                if min_h > graph[ny][nx]:
                    next_y, next_x = ny, nx
                    min_h = graph[next_y][next_x]
    
    # 이동 안했으면
    if next_x == -1:
        dp[y][x] = 1
    
    # 이동 했으면 
    else:
        dp[y][x] = 1 + trail(next_y, next_x)
    
    return dp[y][x]


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]


    ans = 0
    for y in range(n):
        for x in range(n):
            ans = max(ans, trail(y, x))

    print(f"#{tc} {ans}")