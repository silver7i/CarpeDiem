# 오목 판정


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    flag = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                cnt1 = 0
                cnt2 = 0
                cnt3 = 0
                cnt4 = 0

                for x in range(5):
                    # 가로
                    if j+x < N and arr[i][j+x] == 'o':
                        cnt1 += 1
                        if cnt1 == 5:
                            flag = 1
                            break

                    # 세로
                    if i+x < N and arr[i+x][j] == 'o':
                        cnt2 += 1
                        if cnt2 == 5:
                            flag = 1
                            break

                    # \ 대각선
                    if i+x < N and j+x < N and arr[i+x][j+x] == 'o':
                        cnt3 += 1
                        if cnt3 == 5:
                            flag = 1
                            break

                    # / 대각선
                    if i-x >= 0 and j+x < N and arr[i-x][j+x] == 'o':
                        cnt4 += 1
                        if cnt4 == 5:
                            flag = 1
                            break

            if flag:
                break
        if flag:
            break

    if flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')