import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def check(nums, nums_idx, now_value, plus, minus, mul, div, min_max):
    if nums_idx == len(nums):
        min_max[0] = min(min_max[0], now_value)
        min_max[1] = max(min_max[1], now_value)
        return True
    
    if plus > 0:
        check(nums, nums_idx+1, now_value + nums[nums_idx], plus - 1, minus, mul, div, min_max)
    if minus > 0:
        check(nums, nums_idx+1, now_value - nums[nums_idx], plus, minus-1, mul, div, min_max)
    if mul > 0:
        check(nums, nums_idx+1, now_value * nums[nums_idx], plus, minus, mul-1, div, min_max)
    if div > 0:
        check(nums, nums_idx+1, int(now_value / nums[nums_idx]), plus, minus, mul, div-1, min_max)

    return False
                
            

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    'operator_nums = 각 연산자의 개수 +, -, *, /'
    operator_nums = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    min_max = [100000, -100000]
    
    # 연산자 자리가 다 채워질 동안 재귀하면서 nums 인덱스가 연산자자리랑 같으면 minmax 계산
  
    check(nums, 1, nums[0], operator_nums[0], operator_nums[1], operator_nums[2], operator_nums[3], min_max)
    print(f'#{tc} {min_max[1]-min_max[0]}')
    