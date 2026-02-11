# 고대 유적


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Max = -21e8

    def count(i,j):
        count = 0
        row = 0  # 가로
        for x in range(M):
            if j+x<M and arr[i][j+x] == 1:
                row += 1
            else:
                break
        columm = 0  # 세로
        for x in range(N):
            if i+x<N and arr[i+x][j] == 1:
                columm += 1
            else:
                break
        if row > columm:
            count = row
        else:
            count = columm
        return count


    for i in range(N):  # 행
        for j in range(M):  # 열
            if arr[i][j] == 1:  # 시작
                result = count(i,j)
                if result > Max:
                    Max = result

    print(f'#{tc} {Max}')