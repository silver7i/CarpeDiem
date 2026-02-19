import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################
'''
def find_palind(arr, find_len, i, j):
    is_palind = False
    for k in range(j, find_len // 2):
        if arr[i][k] == arr[i][k + (find_len - 1 * k)]:  # 행 / 앞쪽 인덱스와 뒤쪽 인덱스 비교
            print(k, k + (find_len - 1 * k))
            is_palind = True
        else:
            is_palind = False

    return is_palind

T = 10
for test_case in range(1, T + 1):
    find_len = int(input())
    arr_size = 8
    arr = [list(input()) for _ in range(arr_size)]

    # 이중 for 문을 돌면서 홀짝 차이에 따라서 분류
    # 첫번째 인덱스와 대치되는 반대 인덱스 값 비교
    print(arr)
    cnt_palind = 0
    R_is_palind = False
    C_is_palind = False

    for i in range(len(arr) - find_len + 1):
        for j in range(i, len(arr)):
            R_is_palind = find_palind(arr, find_len, i, j)    # 행
            C_is_palind = find_palind(arr, find_len, j, i)    # 열

        if R_is_palind:
            cnt_palind += 1
        if C_is_palind:
            cnt_palind += 1
    print(cnt_palind)
'''

'''
def find_palind_row(arr, find_len, i, j):
    for k in range(find_len // 2):
        if arr[i][j + k] != arr[i][j + (find_len - 1) - k]:  # 행 / 앞쪽 인덱스와 뒤쪽 인덱스 비교
            return 0
    return 1

def find_palind_col(arr, find_len, i, j):
    for k in range(find_len // 2):
        if arr[j + k][i] != arr[j + (find_len - 1) - k][i]:  # 행 / 앞쪽 인덱스와 뒤쪽 인덱스 비교
            return 0
    return 1


T = 10
for test_case in range(1, T + 1):
    find_len = int(input())
    arr_size = 8
    arr = [list(input()) for _ in range(arr_size)]
    
    # 첫번째 인덱스와 대치되는 반대 인덱스 값 비교
    
    cnt_palind = 0

    for i in range(arr_size):
        for j in range(arr_size - find_len + 1):
            cnt_palind += find_palind_row(arr, find_len, i, j)    # 행        
            cnt_palind += find_palind_col(arr, find_len, i, j)    # 열

    print(f'#{test_case} {cnt_palind}')

'''

def find_palind(arr, find_len, i, j):
    for k in range(find_len // 2):
        if arr[i][j+k] != arr[i][j + (find_len - 1) - k]:  # 행 / 앞쪽 인덱스와 뒤쪽 인덱스 비교
            return 0
    return 1


T = 10
for test_case in range(1, T + 1):
    find_len = int(input())
    arr_size = 8
    arr_R = [list(input()) for _ in range(arr_size)]
    arr_C = list(zip(*arr_R))

    # 첫번째 인덱스와 대치되는 반대 인덱스 값 비교
    
    cnt_palind = 0

    for i in range(len(arr_R)):
        for j in range(len(arr_R)-find_len+1):
            cnt_palind += find_palind(arr_R, find_len, i, j)    # 행        
            cnt_palind += find_palind(arr_C, find_len, i, j)    # 열

    print(f'#{test_case} {cnt_palind}')