import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

def my_bin_search(target, end):
    start = 1
    cnt = 0
    while start < end:
        mid = (start + end) // 2
        cnt += 1
        if mid == target:
            return cnt
        elif mid > target:
            end = mid
        else:
            start = mid
    
    return -1


T = int(input())
for test_case in range(1, T + 1):
    P, PA, PB = map(int, input().split())

    A_cnt = my_bin_search(PA, P)
    B_cnt = my_bin_search(PB, P)

    result = 0
    if A_cnt == B_cnt or A_cnt == -1 or B_cnt == -1:
        result = 0
    elif A_cnt < B_cnt:
        result = 'A'
    else:
        result = 'B'

    print(f'#{test_case} {result}')