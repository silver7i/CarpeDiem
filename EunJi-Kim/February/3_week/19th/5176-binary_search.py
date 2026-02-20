import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def make_tree(N, far, a):   # a = 내 왼쪽(먼저 처리된 쪽)에 있는 노드들이 마지막으로 가져간 번호
    if far > N: # 존재하지 않는 자식이면
        return 0
    
    left = make_tree(N, far*2, a) 
    tree[far] = left + a + 1
    right = make_tree(N, far*2+1, tree[far])
    return left + right + 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    make_tree(N, 1, 0)

    print(f'#{tc}', tree[1], tree[N//2]) # 루트에 저장된 값, N/2번 노드에 저장된 값
