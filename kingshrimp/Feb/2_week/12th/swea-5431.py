import sys

sys.stdin = open('swea-5431i.txt')





T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    # 집합을 이용을 해보자
    scores_data = set(map(int, input().split()))
    default = set(range(1,N+1))

    # 차집합 오퍼레이터로 빼기
    not_submitted = default - scores_data
    res = not_submitted
    print(f"#{tc}", *res)