# 미로찾기 (미로)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    flag = 0
    st_x, st_y = -1, -1
    ed_x, ed_y = -1, -1
    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                st_x, st_y = i, j
            elif arr[i][j] == '3':
                ed_x, ed_y = i, j
                   
    def find(x,y):
        global flag
        if x == ed_x and y == ed_y:
            flag = 1
            return
        
        for z in range(4):
            dx = x+di[z]
            dy = y+dj[z]
            if 0<=dx<N and 0<=dy<N:
                if visited[dx][dy] == 0 and arr[dx][dy] != '1':
                    visited[dx][dy] = 1
                    find(dx, dy)
                    if flag == 1:
                        return
                
    visited[st_x][st_y] = 1
    find(st_x, st_y)

    if flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

