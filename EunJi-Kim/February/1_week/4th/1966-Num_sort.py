import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

## 거품정렬
def Bubble_sort(arr):
    N = len(arr)
    for i in range( N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]

## 선택정렬
def Selection_sort(arr):
    N = len(arr)
    for i in range(N-1):
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    #Bubble_sort(arr)
    Selection_sort(arr)

    print(f'#{test_case}', *arr)
    # join은 문자열 메서드여서 map을 통해 str로 변환 후 가능
    #print(f'#{test_case} {" ".join(map(str, arr))}')