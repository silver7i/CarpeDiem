# ===
# 1. 브레인 스토밍
# 돌려 그리고
# ===

import sys

sys.stdin = open('swea-1860i.txt')


# 가로행으로 쭉 풀고 zip으로 돌리고 또 돌려
def solve(N, K, matrix):

    return total

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    res = solve(N, K, matrix)
    print(f'#{tc} {res}')




