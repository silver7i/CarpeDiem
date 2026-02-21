import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################
'''
1-가위 / 2-바위 / 3-보
A-B = 
1 2  -1 => B
1 3  -2 => A
2 1   1 => A
2 3  -1 => B
3 1   2 => B
3 2   1 => A
A(-2, 1)
B(-1, 2)
'''

def tournament(left_arr, right_arr):
    # 만약 1:1 상황이 됐으면 가위바위보 결과 도출
    if len(left_arr) == 1 and len(right_arr) == 1:
        left = left_arr.pop()
        right = right_arr.pop()
        if left == right:
            return left
        elif left - right in [-2, 1]:
            return left
        else:
            return right
    elif len(left_arr) == 1 and len(right_arr) != 1:
        return left_arr.pop()
    
    # 1:1이 안나왔으면 배열을 돌리면서 1:1이 되도록 설정
    while len(left_arr) > 1:
        if len(left_arr) >= 2:
            left_arr.append(tournament(left_arr[:len(left_arr)//2], left_arr[len(left_arr)//2:]))
        if len(right_arr) >= 2:
            right_arr.append(tournament(right_arr[:len(right_arr)//2], right_arr[len(right_arr)//2:]))
        
        if len(left_arr) == 1 and len(right_arr) == 0:
            return left_arr.pop()

T = int(input())
for test_case in range(1, T+1):  
    N = int(input())
    arr = list(map(int, input().split()))

    result = tournament(arr[:len(arr)//2], arr[len(arr)//2:])
    print(result)
