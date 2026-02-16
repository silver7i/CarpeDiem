import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def check(op_arr, op_index, nums, nums_index, min_max):
    if ' ' not in nums:
        left = int(nums[0])
        for i in range(len(nums)):
            if nums[i] == '+':
                left += int(nums[i+1])
            elif nums[i] == '-':
                left -= int(nums[i+1])
            elif nums[i] == '*':
                left *= int(nums[i+1])
            elif nums[i] == '/':
                left //= int(nums[i+1])
        min_max[0] = min(min_max[0], left)
        min_max[0] = max(min_max[1], left)
        return True

    for i in range(op_index, len(op_arr)):
        for j in range(i, len(op_arr)):
            nums[nums_index] = op_arr[j]    # 연산자 넣기
            # 만약 연산자가 다 채워졌다면 
            if check(op_arr, i+1, nums, nums_index+2, min_max):
                nums[nums_index] = ' '
    
    return True
                
                


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    'operator_nums = 각 연산자의 개수 +, -, *, /'
    operator_nums = list(map(int, input().split()))
    '숫자, ' ', 숫자, ' ' 형태로 들어오도록'
    nums = list(map(str, input().strip()))

    operator_arr = ['+'] * operator_nums[0]
    operator_arr += ['-'] * operator_nums[1]
    operator_arr += ['*'] * operator_nums[2]
    operator_arr += ['/'] * operator_nums[3]
    
    min_max = [10000, 0]
    
    check(operator_arr, 0, nums, 1, min_max)
    print(min_max)
    