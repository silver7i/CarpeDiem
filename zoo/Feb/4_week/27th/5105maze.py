dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(start_y, start_x):
    queue = [(start_y, start_x)] # 큐 생성
    visited = [[0] * N for _ in range(N)] # 방문 배열 생성
    visited[start_y][start_x] = 1 # 시작점 방문 표시
    front = 0 # 큐 dequeue 포인터 생성
    while front < len(queue): # front가 queue 끝까지 갈 때까지
        curr_y, curr_x = queue[front] # dequeue 
        if maze[curr_y][curr_x] == 3:
            return visited[curr_y][curr_x] - 2
        front += 1 # 포인터 다음으로 이동
        for d in range(4):
            nxt_y = curr_y + dy[d]
            nxt_x = curr_x + dx[d]
            # 인덱스 범위 벗어나는 거 방지
            if 0 <= nxt_y < N and 0 <= nxt_x < N:
                # 미로에서 벽이 아니고 방문한 적이 없는 곳이면
                if maze[nxt_y][nxt_x] != 1 and visited[nxt_y][nxt_x] == 0:
                    queue.append((nxt_y, nxt_x)) # 방문 가능한 곳 enqueue
                    # 방문가능한 곳에 기존 거리에서 +1
                    visited[nxt_y][nxt_x] = visited[curr_y][curr_x] + 1

    return 0 # 경로가 없는 경우    
        
    

def find_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
                

t = int(input())

for tc in range(1, t+1):
    N = int(input()) # 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)] # 미로 입력 받기
    
    # 출력 -> 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지
    # 경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸수, 경로가 없는 경우 0
    
    """
    필요한 것
    시작점 좌표
    방문록에 이동시마다 기존칸 + 1 찍기
    """
    sy, sx = find_start()
    ans = bfs(sy, sx)
    
    print(f"#{tc} {ans}")