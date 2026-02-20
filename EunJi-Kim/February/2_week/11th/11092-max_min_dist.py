import sys
from pathlib import Path
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = [arr[0], 0]
    min_num = [arr[0], 0]
    for i in range(len(arr)):
        if max_num[0] <= arr[i]: # 큰수가 여러개이면 마지막에 나오는 걸로 하기 위해 <=
            max_num[0] = arr[i]
            max_num[1] = i
        
        if min_num[0] > arr[i]: # 작은수가 여러개이면 먼저 나오는 걸로 하기 위해 >
            min_num[0] = arr[i]
            min_num[1] = i

    sub_abs = abs(max_num[1]-min_num[1])
    print(f'#{test_case} {sub_abs}')
    