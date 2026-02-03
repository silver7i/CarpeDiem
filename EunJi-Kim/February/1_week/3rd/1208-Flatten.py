import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################


#1.

# 제일 높은 곳과 제일 낮은 곳의 인덱스를 찾아서
# 제일 높은 곳은 -1, 제일 낮은 곳은 +1

N = 100
T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    arr = list(map(int, input().split()))

    # 오름차순으로 정렬을 해서
    arr.sort()
    # dump 가능 횟수만큼 돌고
    for i in range(dump):
        # 최고는 빼고 최소는 더해서 다시 정렬
        # sort() 를 한번 더 하면 0번 자리와 끝자리는 항상 최소와 최대
        arr[0] += 1
        arr[-1] -= 1
        arr.sort()

        if arr[-1] - arr[0] <= 1:
            break

    print(f'#{test_case} {arr[-1] - arr[0]}')
    

############################################
'''
#2. 버블 정렬 연습

def my_sort(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


N = 100
T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    arr = list(map(int, input().split()))

    my_sort(arr, len(arr))           # => arr.sort()
    for i in range(dump):
        arr[0] += 1
        arr[-1] -= 1
        my_sort(arr, len(arr))        # => arr.sort()

    print(f'#{test_case} {arr[-1] - arr[0]}')

'''