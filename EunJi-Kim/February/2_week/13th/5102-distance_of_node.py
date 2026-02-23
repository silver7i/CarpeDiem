import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def bfs(arr, now, G):
    visited = [0] * (V+1)
    queue = [now]

    while queue:
        now = queue.pop(0)
        if now == G:
            return visited[now]
        
        for ni in arr[now]:
            if visited[ni] == 0:
                queue.append(ni)
                visited[ni] += visited[now] + 1

    return 0

        
T = int(input())
for test_case in range(1, T+1): 
    V, E = map(int, input().split())    # V : 노드 개수, E : 간선 개수
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int , input().split())

    adj_list = [[] for _ in range(V+1)]
    for i in range(len(arr)):
        v1, v2 = arr[i]
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    cnt = bfs(adj_list, S, G)

    print(f'#{test_case}', cnt)




