import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


# 완전트리가 아니었다는 함정!!!!!! 
# 왼쪽 오른쪽 자식을 연산자랑 함께 리스트로, 같은 인덱스에 저장하는 팁!!

def calculate(N, par):
    if len(tree[par]) == 1:
        return int(tree[par][0])
    
    left = calculate(N, tree[par][1])
    right = calculate(N, tree[par][2])
    mid = tree[par][0]
    if mid == '+':
        return left + right
    elif mid == '-':
        return left - right
    elif mid == '*':
        return left * right
    elif mid == '/':
        return left / right


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]   # str로 받음

    tree = [[0] for _ in range(N+1)]

    for i in range(N):
        tree[int(arr[i][0])][0] = arr[i][1]
        if arr[i][1] in '+-*/':
            tree[int(arr[i][0])].append(int(arr[i][2]))
            tree[int(arr[i][0])].append(int(arr[i][3]))
            
    result = int(calculate(N, 1))

    print(f'#{tc}', result)
