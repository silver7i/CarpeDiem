# 파스칼의 삼각형


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1

    for i in range(1, N):
        arr[i][0] = 1
        for j in range(1, N):
            if arr[i-1][j] == 0:
                arr[i][j] = 1
                break
            else:
                arr[i][j] = arr[i-1][j-1]+arr[i-1][j]  # 11시+12시 값

    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j],end=' ')
        print()
