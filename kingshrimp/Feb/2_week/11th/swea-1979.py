# ===
# 1. 브레인 스토밍
# 돌려 그리고
# ===

import sys

sys.stdin = open('swea-1979i.txt')


# 가로행으로 쭉 풀고 zip으로 돌리고 또 돌려
def solve(N, K, matrix):
    total = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if matrix[i][j] == 1:
                cnt += 1
            else:
                #  벽을 만나면 추가
                if cnt == K:
                    total += 1
                    cnt = 0
                else:
                    cnt = 0
        #  다 돌았을때도 체크해야해
        if cnt == K:
            total +=1

    new_matrix = [list(row) for row in zip(*matrix)]
    for i in range(N):
        cnt = 0
        for j in range(N):
            if new_matrix[i][j] == 1:
                cnt += 1
            else:
                #  벽을 만나면 추가
                if cnt == K:
                    total += 1
                    cnt = 0
                else:
                    cnt = 0
        #  다 돌았을때도 체크해야해
        if cnt == K:
            total +=1
    return total

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    res = solve(N, K, matrix)
    print(f'#{tc} {res}')




