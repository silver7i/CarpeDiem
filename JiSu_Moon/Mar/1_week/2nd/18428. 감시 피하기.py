N = int(input())
arr = [list(input().split()) for _ in range(N)]

di = [-1,1,0,0]
dj = [0,0,-1,1]
cnt = 0

for i in range(N):
    for j in range(N):
        # 선생님 찾기
        if arr[i][j] == 'T':
            for d in range(4):
                for power in range(1, N):
                    dy = i+di[d]*power
                    dx = j+dj[d]*power
                    if 0<=dy<N and 0<=dx<N:
                        if arr[dy][dx] == 'O':
                            break
                        # 학생 찾기
                        if power == 1 and arr[dy][dx] == 'S':
                            cnt = 4
                            break

                        elif arr[dy][dx] == 'S':
                            # 상
                            if di[d] == -1:
                                arr[dy+1][dx] = 'O'
                                cnt += 1
                            # 하
                            elif di[d] == 1:
                                arr[dy-1][dx] = 'O'
                                cnt += 1
                            # 좌
                            elif dj[d] == -1:
                                arr[dy][dx+1] = 'O'
                                cnt += 1
                            # 우
                            elif dj[d] == 1:
                                arr[dy][dx-1] = 'O'
                                cnt += 1
                            break

if cnt > 3:
    print('NO')
else:
    print('YES')
