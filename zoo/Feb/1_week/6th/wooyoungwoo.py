T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]


    # 행 기준
    for y in range(N):
        for x in range(N):
            check_list = []
            for p in range(x, N):
                check_list.append(arr[y][p])
            if len(check_list) == M:
                check_str = ''.join(check_list)
        if check_str == check_str[::-1]:
            print(f"#{tc} {check_str}")

    # 열 기준
    for x in range(N):
        for y in range(N):
            check_list = []
            for p in range(y, N):
                check_list.append(arr[p][x])
            if len(check_list) == M:
                check_str = ''.join(check_list)
        if check_str == check_str[::-1]:
            print(f"#{tc} {check_str}")