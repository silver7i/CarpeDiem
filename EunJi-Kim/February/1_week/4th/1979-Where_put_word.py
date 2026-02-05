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
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        col_cnt = 0
        row_cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                col_cnt += 1
                if j == N-1 and col_cnt == K:
                    result += 1
            else:
                if col_cnt == K:
                    result += 1
                col_cnt = 0
            
            if arr[j][i] == 1:
                row_cnt += 1
                if j == N-1 and row_cnt == K:
                    result += 1
            else:
                if row_cnt == K:
                    result += 1
                row_cnt = 0

    print(f'#{test_case} {result}')