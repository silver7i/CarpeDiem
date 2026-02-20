import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def find_min_sum(arr, i, now_sum, visited):
    global min_sum

    if now_sum > min_sum:
        return

    if i == len(arr):
        min_sum = min(min_sum, now_sum)
        return

    for j in range(len(arr[i])):
        if not visited[j]:
            now_sum += arr[i][j]
            visited[j] = True
            find_min_sum(arr, i+1, now_sum, visited)
            now_sum -= arr[i][j]
            visited[j] = False

T = int(input())
for test_case in range(1, T+1):  
    N = int(input())
    arr = [ list(map(int, input().split())) for _ in range(N)]
    
    visited = [False] * N
    min_sum = 100000
    now_sum = 0
    find_min_sum(arr, 0, now_sum, visited)

    print(f'#{test_case}', min_sum)