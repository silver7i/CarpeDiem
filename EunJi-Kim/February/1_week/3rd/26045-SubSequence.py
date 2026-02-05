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
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    cnt = 0
    # A를 순회하면서
    for i in range(N):
        # A의 요소가 B의 요소랑 같으면 cnt 값을 늘려서 B의 인덱스를 변경
        if A_arr[i] == B_arr[cnt]:
            cnt += 1
        # cnt 값이 B의 길이와 같으면 for문 탈출
        if len(B_arr) == cnt:
            break

    if len(B_arr) == cnt:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')