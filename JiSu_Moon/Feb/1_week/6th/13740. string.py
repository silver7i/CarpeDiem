# 회문 (String) 


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 가로탐색
    for x in range(N):  # 행
        for i in range(N-M+1):  # 행에서 탐색 범위
            for j in range(M//2):  # 회문 범위
                if arr[x][i+j] != arr[x][i+M-1-j]:
                    break
            else:  # 다 돌았는데 회문이면
                print(f'#{tc}',''.join(arr[x][i:i+M]))
    # 세로탐색
    for y in range(N):  # 열
        for i in range(N-M+1):  # 열에서 탐색 범위
            for j in range(M//2):  # 회문 범위
                if arr[i+j][y] != arr[i+M-1-j][y]:
                    break
            else:  # 다 돌았는데 회문이면
                print(f'#{tc}',''.join(arr[i+r][y] for r in range(M)))
