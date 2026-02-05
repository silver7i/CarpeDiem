import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

T = 10
for test_case in range(1, T + 1):
    test_case = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 각 세트의 합에서 큰 값은 max_sum 변수로 갱신 해서 큰 값 찾기
    max_sum = 0
    diagonal_sum1 = 0
    diagonal_sum2 = 0
    # 각 행을 돌면서
    for i in range(N):
        # 각 행의 최대값을 찾음
        row_sum = sum(arr[i])
        if max_sum < row_sum:
            max_sum = row_sum

        # 열의 합을 구할 거임 # 열과 행의 크기가 다르면????? 은 나중에 생각해보자
        col_sum = 0
        for j in range(N):
            col_sum += arr[j][i]
        if max_sum < col_sum:
            max_sum = col_sum

        # 대각선의 합 구하기

        diagonal_sum1 += arr[i][i]
        diagonal_sum2 += arr[i][N-1-i]

    max_sum = max(max_sum, diagonal_sum1, diagonal_sum2)

    print(f'#{test_case} {max_sum}')
