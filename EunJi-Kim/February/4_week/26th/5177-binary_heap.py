import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    for i in range(2, N+1):
        current = i
        while i > 1:
            parent = current // 2
            if arr[current] < arr[parent]:
                arr[current], arr[parent] = arr[parent], arr[current]
                current = parent
            else:
                break

    cnt = 0
    current = N // 2    # 마지막 노드의 부모부터 시작
    while current > 0:
        cnt += arr[current]
        current //= 2

    print(f'#{tc}', cnt)
