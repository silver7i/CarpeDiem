import sys
from pathlib import Path
file_name = Path(__file__).stem
sys.stdin = open(f"./input_src/{file_name}.txt")


T = 10
for test_case in range(1, T + 1):

    N = int(input())    # 건물 수
    input_arr = list(map(int, input().split())) # 층수 있는 건물 배열

    arr = []
    # 층수가 있으면 1, 없으면 0 인 2중 배열을 만들자.
    for i in range(N):
        inner_list = []
        for j in range(1, 256):
            if j < input_arr[i]+1:
                inner_list.append(1)
            else:
                inner_list.append(0)
        arr.append(inner_list)

    # 이제 비교를 해보자
    cnt = 0
    for i in range(N):
        # 층수만큼 돌면서
        for j in range(len(arr[i])):
            # 양 옆을 찾아
            # 같은 층 인덱스 찾으려면 인덱스가 있어야 하니까 양 옆의 인덱스 확인.
            if arr[i][j] == 1:
                if arr[i-1][j] != 1 and arr[i-2][j] != 1 and arr[i+1][j] != 1 and arr[i+2][j] != 1:
                    cnt += 1
    print(f'#{test_case} {cnt}')