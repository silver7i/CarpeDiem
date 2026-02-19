import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def in_order(node, result):
    if node:
        in_order(left[node], result)
        result.append(node_value[node])
        in_order(right[node], result)

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    # 노드 번호별 단어 저장
    node_value = [''] * (N+1)
    for i in range(N):
        node_value[int(arr[i][0])] = arr[i][1]

    # 부모번호를 인덱스로 저장하는 배열
    left = [0] * (N + 1) # 루트 정점은 항상 1
    right = [0] * (N + 1)

    for i in range(N):
        par_num = int(arr[i][0])
        
        if len(arr[i])>=3 and left[par_num] == 0:   # arr[i][0] == 정점 번호
            left_node = int(arr[i][2])
            left[par_num] = left_node
        
        if len(arr[i])>=4 and right[par_num] == 0:
            right_node = int(arr[i][3])
            right[par_num] = right_node        

    result = []
    in_order(1, result)
    print(f'#{tc}', ''.join(result))
