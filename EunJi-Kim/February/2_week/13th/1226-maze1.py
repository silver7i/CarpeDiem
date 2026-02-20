import sys
from pathlib import Path

file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)

sys.stdin = open(file_path, "r")

##############################
# y, x
deltas = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
]
def bfs(arr, now, end):
    visited = [[0]*16 for _ in range(16)]   # visited 생성
    q = [now]             # 큐 생성 # 시작점 인큐
    visited[now[0]][now[1]] = 1    # 시작점 인큐 visited 표시
    while q:    
        # 디큐해서 인접한 통로 찾기
        now = q.pop()
        for direc in range(4):
            ny = now[0] + deltas[direc][1]
            nx = now[1] + deltas[direc][0]
            if visited[ny][nx] == 0 and arr[ny][nx] == 0:
                q.append([ny, nx])
                visited[ny][nx] = visited[now[0]][now[1]] + 1
            elif arr[ny][nx] == 3:
                return 1
    return 0
            

T = 10
for test_case in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    start = [-1,-1]     # y, x
    end = [-1,-1]
    for y in range(16):
        for x in range(16):
            if maze[y][x] == 2:
                start = [y, x]
            elif maze[y][x] == 3:
                end = [y, x]

    print(f'#{tc}', bfs(maze, start, end))