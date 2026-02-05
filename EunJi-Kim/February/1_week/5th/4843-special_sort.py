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
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        if i % 2 == 0:
            for j in range(i+1, N):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        else:
            for j in range(i+1, N):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

    print(f'#{test_case}', *arr[:10])

