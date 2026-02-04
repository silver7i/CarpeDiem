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
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            sum_kill = 0
            for k in range(M):
                for l in range(M):
                    sum_kill += arr[i+k][j+l]

            max_sum = max(max_sum, sum_kill)

    print(f'#{test_case} {max_sum}')
