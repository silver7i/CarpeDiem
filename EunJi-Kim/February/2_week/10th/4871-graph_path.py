import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def my_dfs(start_node, Goal_node, adj_arr, visited_arr): # 출발-도착 세트 리스트를 돌면서
    result = 0
    visited_arr[start_node] = 1 # 시작 노드 방문체크

    if start_node == Goal_node:
        return 1
    elif not adj_arr[start_node]: # 빈 리스트이면(다음이 없으면)
        return 0
    else:
        for next_node in adj_arr[start_node]:
            if visited_arr[next_node] == 0:  # 방문했던 적이 없으면
                result = my_dfs(next_node, Goal_node, adj_arr, visited_arr)
                if result == 1:
                    return 1
    return 0    # next_node 가 다 방문했던 적이 있다면

T = int(input())
for test_case in range(1, T + 1):
    V_node, E_line = map(int, input().split())      # V 개의 노드 / E 개의 간선
    s_n_arr = [list(map(int, input().split())) for _ in range(E_line)]  # 출발(start) | 도착(next) 리스트
    S_node, G_node = map(int, input().split())  # 시작 노드 | 도착 노드

    adj_list = [[] for _ in range(V_node + 1)] 
    visited_arr = [ 0 for _ in range(V_node + 1)]

    for s_n in s_n_arr: # 출발-도착 세트 리스트를 돌면서
        adj_list[s_n[0]].append(s_n[1]) # 인접리스트에 시작점을 인덱스로 해서 도착점 노드를 넣음
    result = my_dfs(S_node, G_node, adj_list, visited_arr)
    
    print(f'#{test_case} {result}')