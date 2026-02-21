import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


T = 10
for test_case in range(1, T+1):  
    t = int(input())
    arr = list(map(int, input().split()))

    rear = len(arr)-1
    front = 0
    cnt = 0
    while arr[rear] > 0: # 배열의 맨 뒤의 숫자가 0이 아닌 동안
        if cnt >= 5:
            cnt = 0
        cnt += 1
        
        arr[front] -= cnt
        if arr[front] <= 0:
            arr[front] = 0
    
        arr.append(arr[front])
        front += 1
        rear += 1
    
    print(f'#{test_case}', *arr[front:rear+1])



