T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_v, min_v = 0, int(1e9)

    for i in range(N-M+1):
        s = 0
        for j in range(i, i+M):
            s += arr[j]

        if max_v < s:
            max_v = s

        if min_v > s:
            min_v = s

    print(f"#{tc} {max_v - min_v}")