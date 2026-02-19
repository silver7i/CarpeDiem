import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / "26045-SubSequence.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################



T = int(input())
for test_case in range(1, T + 1):
    A_len, B_len = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    check_index = 0
    for i in A_arr:
        if i == B_arr[check_index]:
            check_index += 1
        
        if check_index >= B_len:
            break

    if check_index == B_len:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')