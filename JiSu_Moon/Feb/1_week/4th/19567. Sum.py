# Sum


for _ in range(1,11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    Max = -21e8

    for i in range(100):
        Sum1 = 0  # 가로
        Sum2 = 0  # 세로
        Sum3 = 0  # \
        Sum4 = 0  # /

        for j in range(100):
            Sum1 += arr[i][j]
            Sum2 += arr[j][i]
            Sum3 += arr[j][j]
            Sum4 += arr[j][100 - j - 1]
        max_sum = max(Sum1, Sum2, Sum3, Sum4)
        if max_sum > Max:
            Max = max_sum

    print(f'#{T} {Max}')

