import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

deltas = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
]

def bfs(maze, N, now, goal):
    visited = [[0] * N for _ in range(N)]
    queue = [now]

    result = 0
    while queue:
        now = queue.pop(0)

        for i in range(4):
            ni = now[0] + deltas[i][0]
            nj = now[1] + deltas[i][1]
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                if maze[ni][nj] == '0':
                    queue.append([ni, nj])
                    visited[ni][nj] = visited[now[0]][now[1]] + 1
                elif maze[ni][nj] == goal:
                    result = visited[now[0]][now[1]]
                    break
                
        if result != 0:
            return result
    
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]  # 0:통로, 1:벽, 3:도착

    now = [-1, -1]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                now = [i, j]

    print(f'#{tc}', bfs(maze, N, now, '3'))
