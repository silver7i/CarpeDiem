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

stack = [] # 이긴 사람 넣기
def tournament(arr, start, end):
    mid = (start + end) // 2
    left = arr[:mid+1]
    right = arr[mid+1:]

    if start == end:
        return left
    elif end - start == 1:
        if left[0][1] == right[0][1]:
            return left
        elif left[0][1] - right[0][1] in [-2, 1]:
            return left
        elif left[0][1] - right[0][1] in [-1, 2]:
            return right
    
    while end - start > 1:
        left_winner = tournament(left, 0, len(left)-1)
        right_winner = tournament(right, 0, len(right)-1)  
        final = tournament(left_winner + right_winner, 0, 1) 
        return final   
    
    return 0

T = int(input())
for test_case in range(1, T+1):  
    N = int(input())
    arr = list(map(int, input().split()))
    
    cards = []
    for i in range(N):
        cards.append([i+1, arr[i]])

    winner = tournament(cards, 0, N-1)    
    print(f'#{test_case}', winner[0][0])
    
    
