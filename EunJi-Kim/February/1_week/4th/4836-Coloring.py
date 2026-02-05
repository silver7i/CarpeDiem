import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

'''
    (r1, c1) ..길이: c2-c1+1.. (r1, c2)
    ...                         ...
 길이 : r2-r1+1               길이 : r2-r1+1
    ...                         ...
    (r2, c1) ..길이 : c2-c1+1.. (r2, c2) 
'''

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0 for _ in range(10)]for _ in range(10)]

    # 색칠할 네모 개수만큼 돌기
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # 색칠할 네모 행 순회
        for i in range(r1, r2+1):
            # 열 순회
            for j in range(c1, c2+1):
                # 만약 color 값보다 arr의 요소가 작을때만 색칠
                # 만약 요소의 값이 3보다 작거나 요소에서 color를 뺀 값이 0이 아니면 더하기
               if arr[i][j] < 3 and arr[i][j] - color != 0:
                    arr[i][j] += color
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] >= 3:
                cnt += 1

    print(f'#{test_case} {cnt}')