import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

T = int(input())
for test_case in range(1, T + 1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]

    is_correct = 1
    # 세트의 길이가 N이면 1, 아니면 0
    for i in range(N):
        col_set = set()
        row_set = set()
        for j in range(N):
            row_set.add(arr[i][j])
            col_set.add(arr[j][i])

        if len(row_set) != N or len(col_set) != N:
            is_correct = 0
            break

    for i in range(0, 9, 3):
        rec_set = set()
        for j in range(3):
            for k in range(3):
                rec_set.add(arr[j][k])
        if len(rec_set) != N:
            is_correct = 0

    print(f'#{test_case} {is_correct}')
