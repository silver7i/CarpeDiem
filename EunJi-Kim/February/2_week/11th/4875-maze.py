import sys
from pathlib import Path

file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)

sys.stdin = open(file_path, "r")

##############################

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    
    # 현 위치 찾기
    now = [-1, -1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                now = [i, j]

    deltas = [
        [0, 1],
        [1, 0],
        [0, -1],
        [-1, 0],
    ]

    visited = [[0]*N for _ in range(N)]
    stack = [now]
    result = 0

    while 1:
        for j in range(4):
            ni = now[0] + deltas[j][0]
            nj = now[1] + deltas[j][1]
            # 미로 범위 안에 있고, 방문한적이 없고, 벽이 아니라면
            if 0 <= ni <= N-1 and 0 <= nj <= N-1\
                and visited[ni][nj] == 0\
                    and arr[ni][nj] != 1:
                if arr[ni][nj] == 0:
                    stack.append([ni, nj])
                elif arr[ni][nj] == 3:
                    result = 1
                    break

        if result == 1:
            break

        now = stack.pop()    
        if arr[now[0]][now[1]] == 2:  # 스택에서 시작점이 나온다는 건 도착점이 없다는 것
            break    
        else:
            visited[now[0]][now[1]] = 1

    print(f'#{tc} {result}')                