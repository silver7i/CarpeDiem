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
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    front = 0
    for i in range(M):
        arr.append(arr[front])
        front += 1      # 뒤에 추가해줬으니 front도 뒤로 이동해서 배열 개수 맞추기

    print(f'#{test_case}', arr[front])
    