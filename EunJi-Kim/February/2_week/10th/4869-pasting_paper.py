import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

def check(N):
    # 끝에 가로 10 막대가 올때 / 가로 20 (막대가 올때 + 네모가 올때)
    if N == 10:
        return 1
    elif N == 20:   # 가로 20 만 남았을 때
        return 3    # 가로10*2 한쌍 + 가로20*2 한쌍 + 가로20네모
    else:
        return check(N-10) + (2 * check(N-20))

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    print(f'#{test_case} {check(N)}')

    