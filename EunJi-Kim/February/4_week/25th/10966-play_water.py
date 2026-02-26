import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


deltas = [
    [0,1],
    [1,0],
    [0,-1],
    [-1,0],
]    

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    visited = [[-1]*M for _ in range(N)]
    q = []
    front = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                visited[i][j] = 0
                q.append((i, j))

    while front < len(q):
        now = q[front]
        front += 1
        now_i, now_j = now[0], now[1]
        
        for k in range(4):
            next_i = now_i + deltas[k][0]
            next_j = now_j + deltas[k][1]

            if 0 <= next_i < N and 0 <= next_j < M and visited[next_i][next_j] == -1:
                visited[next_i][next_j] = visited[now_i][now_j] + 1
                q.append((next_i, next_j))

    total = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != -1:
                total += visited[i][j]

    print(f'#{tc}', total)