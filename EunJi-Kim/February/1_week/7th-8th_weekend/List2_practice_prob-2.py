import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / "List2_practice_prob-1.txt"

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    d_i = [0, 1, 0, -1]  # 동남서북
    d_j = [1, 0, -1, 0]

    # 1.
    # sum_sub = 0
    # for i in range(N):
    #     for j in range(N):
    #         for k in range(4):
    #             if 0 <= i+delt_i[k] < N and 0 <= j+delt_j[k] < N:
    #                 sub = arr[i][j] - arr[i+delt_i[k]][j+delt_j[k]]
    #                 if sub < 0:
    #                     sub = sub * (- 1)
    #                 sum_sub += sub

    # print(sum_sub)

    # 2.
    sum_sub = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + d_i[k]
                nj = j + d_j[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_sub += abs(arr[i][j] - arr[ni][nj])
                    print(sum_sub)

    print(sum_sub)