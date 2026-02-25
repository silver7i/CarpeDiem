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

def find_water(arr, now):
    N, M = len(arr), len(arr[0])
    now_i = now[0]
    now_j = now[1]

    direc_visited = [[0]*M for _ in range(N)]
    q = [now]
    direc_visited[now_i][now_j] = 1

    while q:
        for k in range(4):
            cnt = 0
            now = q.pop(0)
            now_i, now_j = now[0], now[1]
            
            next_i = now_i + deltas[k][0]
            next_j = now_j + deltas[k][1]

            if arr[now_i][now_j] == 'W':
                return find_water(arr, [next_i, next_j])
            else:
                if 0<=next_i<N and 0<=next_j<M and direc_visited[next_i][next_j] == 0:
                    if arr[next_i][next_j] != 'W':
                        q.append([next_i, next_j])
                        direc_visited[next_i][next_j] = direc_visited[now_i][now_j] + 1
                    else:
                        return direc_visited[now_i][now_j]
        cnt += find_water(arr, now)
                
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    visited = [[0]*M for _ in range(N)]

    total = find_water(arr, [0, 0]) 

    print(f'#{tc}', total)
            