t = int(input())

for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    # 시작 위치 찾기
    for y in range(n):
        for x in range(n):
            if graph[y][x] == 2:
                r_y, r_x = y, x # robot_y, robot_x
        
    # 일직선으로 밖에 못감
    # 좌 (y = 0, x = -1)
    lx = r_x - 1
    # 왼쪽 0 이면 왼쪽이 1일때 까지 혹은 끝까지 이동후 1찍자
    if 0 <= lx and graph[r_y][lx] == 0:
        while 0 <= lx and graph[r_y][lx] != 1:
            graph[r_y][lx] = 1
            lx -= 1

    # 우 (y = 0, x = 1)
    rx = r_x + 1
    # 왼쪽 0 이면 왼쪽이 1일때 까지 혹은 끝까지 이동후 1찍자
    if rx < n and graph[r_y][rx] == 0:
        while rx < n and graph[r_y][rx] != 1:
            graph[r_y][rx] = 1
            rx += 1

    # 상 (y = -1, x = 0)
    uy = r_y - 1
    # 왼쪽 0 이면 왼쪽이 1일때 까지 혹은 끝까지 이동후 1찍자
    if 0 <= uy and graph[uy][r_x] == 0:
        while 0 <= uy and graph[uy][r_x] != 1:
            graph[uy][r_x] = 1
            uy -= 1

    # 하 (y = 1, x = 0)
    dy = r_y + 1
    # 왼쪽 0 이면 왼쪽이 1일때 까지 혹은 끝까지 이동후 1찍자
    if dy < n and graph[dy][r_x] == 0:
        while dy < n and graph[dy][r_x] != 1:
            graph[dy][r_x] = 1
            dy += 1

    # 0 세기
    zero_cnt = 0

    for y in range(n):
        for x in range(n):
            if graph[y][x] == 0:
                zero_cnt += 1
    
    print(f"#{tc} {zero_cnt}")