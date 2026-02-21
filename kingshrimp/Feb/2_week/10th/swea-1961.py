# ===
# 1. 아이디어
# 90도 돌리는 함수를 만들자
# 이 함수를 2번을 더 써서 180도 270도를 만들자
# 
# ===


import sys

sys.stdin = open('swea-1961i.txt')

# 90도 돌리는 함수, 이거 뭔가 내가 만들려고 시도를 했는데 최적화 알고리즘이
# 이미 있을것 같아서 적어두었다. 이거 외우자.
def solve(N, matrix):
    new_matrix = [[0]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_matrix[i][j] = matrix[N-1-j][i]
    return N, new_matrix

T = int(input())

for tc in range(1, T+1):
    # 입력은 함수에서 받으면 안됨.
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    rot_90 = (solve(N, arr))
    rot_180 = (solve(*solve(N, arr)))
    rot_270 = (solve(*solve(*solve(N, arr))))

# join메서드는 str만 사용이 가능하다. 따라서 map을 사용해서 한번에 str로 변경
# 진짜 미친 출력... 이게 뭐야 이것도 학습하라고 일부러 출력 이렇게 한건가?
for i in range(N):
        res_90 = "".join(map(str, rot_90[i]))
        res_180 = "".join(map(str, rot_180[i]))
        res_270 = "".join(map(str, rot_270[i]))
        print(f"{res_90} {res_180} {res_270}")