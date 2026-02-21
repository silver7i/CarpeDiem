T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    pascal = [[0] * (N + 1) for _ in range(N)]

    pascal[0][0] = 1

    for i in range(1, N):
        for j in range(i + 1):
            if j == 0:
                pascal[i][j] = pascal[i - 1][j]
            else:
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    print(f"#{tc}")
    for i in range(N):
        row = pascal[i][:i + 1]
        print(*(row))