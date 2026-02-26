T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    stop = [0] + list(map(int, input().split()))

    stop_diff = []
    for m in range(M):
        stop_diff.append(stop[m+1] - stop[m])

    print(stop_diff)

    count = 0

    # 합이 작거나 같을 때까지..
    # 합이 크다 -> 나가리
    # 흠..