import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = str(input())
    
    cnt = 0
    max_cnt = 0
    for i in arr:
        if i == '1':
            cnt += 1
            if max_cnt < cnt:   # cnt 값이 max보다 클때 max_cnt를 바꿔주고
                max_cnt = cnt
        else:                   # 0 이면
            cnt = 0             # cnt 초기화

    print(f'#{test_case} {max_cnt}')
