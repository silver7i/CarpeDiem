import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

cnt = 0
def Subtotal_judgment(arr, now, N, K, sub_set): # 3  6
    if now == len(arr):
        if sum(sub_set) == K and len(sub_set) == N:
            global cnt
            cnt += 1
        return

    Subtotal_judgment(arr, now+1, N, K, sub_set)
    sub_set.append(arr[now])
    Subtotal_judgment(arr, now+1, N, K, sub_set)
    sub_set.pop()

T = int(input())
for test_case in range(1, T + 1):
    cnt = 0
    # N : 부분집합 원소 수  K : 부분 집합의 합
    N, K = map(int, input().split())
    i = 0
    A = list(i for i in range(1, 13))  # A : 1, 2, .., 10, 11, 12

    # 완전 탐색 방법
    Subtotal_judgment(A, 0, N, K, [])

    print(f'#{test_case} {cnt}')