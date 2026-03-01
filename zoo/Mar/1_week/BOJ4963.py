import sys
sys.setrecursionlimit(10000)

# 8방향 탐색
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def find_land(y, x):
    # 현재 땅을 방문 처리
    memo[y][x] = 1 
    
    for d in range(8):
        ny = y + dy[d]
        nx = x + dx[d]
        
        # 지도 범위 안에 있고
        if 0 <= ny < H and 0 <= nx < W:
            # 땅이면서 아직 방문하지 않았다면 재귀 탐색
            if graph[ny][nx] == 1 and memo[ny][nx] == 0:
                find_land(ny, nx)

# 여러 개의 테스트 케이스를 처리하기 위한 무한 루프
while True:
    W, H = map(int, sys.stdin.readline().split())
    
    # 입력의 마지막 줄(0 0)이면 루프 종료
    if W == 0 and H == 0:
        break

    graph = []
    for _ in range(H):
        graph.append(list(map(int, sys.stdin.readline().split())))

    memo = [[0] * W for _ in range(H)]
    cnt = 0 
    
    # 시작점 찾기
    for row in range(H):
        for col in range(W):
            # 방문하지 않은 땅(1)을 만나면 새로운 섬 발견!
            if graph[row][col] == 1 and memo[row][col] == 0:
                find_land(row, col) # DFS를 돌려 연결된 섬을 모두 방문 처리
                cnt += 1            # 하나의 덩어리 탐색이 끝났으므로 섬 개수 + 1

    print(cnt)