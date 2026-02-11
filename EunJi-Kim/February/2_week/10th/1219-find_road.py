import sys
from pathlib import Path

file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)

sys.stdin = open(file_path, "r")

T = 10
for test_case in range(1, T+1):
    node_num = 100
    t, road_N = map(int, input().split())
    input_arr = list(map(int, input().split())) # 0=출발/99=도착

    adj_list = [[] for _ in range(node_num)]
    for i in range(road_N):
        start = input_arr[i * 2]    # 0, 2, 4, 6
        end = input_arr[i * 2 + 1]  # 1, 3, 5, 7

        if len(adj_list[start]) < 2:    # 2갈래가 넘는 쌍은 버려지는 듯?
            adj_list[start].append(end) 

    stack = [0]
    visited = [0 for _ in range(node_num)]

    result = 0
    while stack: # stack이 차있는 동안 루프
        now = stack.pop()

        if now == 99:
            result = 1
            break
        
        if adj_list[now] and visited[now] == 0:  # 다음 노드가 존재하고, 간적 없는 노드일 때
            for i in adj_list[now]: # 현 위치와 이어진 다음 노드들을 하나씩 빼와서
                stack.append(i)     # 스택에 넣음
            visited[now] = 1        # 지금 위치는 갔다고 표시

    print(f'#{test_case} {result}')





