dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def go(y, x):
    stack = [(y, x)]

    while stack:
        y, x = stack.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    stack.append((ny, nx))
                
                elif graph[ny][nx] == 3:
                    return 1

    return 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]

    start_y, start_x = 0, 0

    for y in range(n):
        for x in range(n):
            if graph[y][x] == 2:
                start_y, start_x = y, x
    
    print(f"#{tc} {go(start_y, start_x)}")