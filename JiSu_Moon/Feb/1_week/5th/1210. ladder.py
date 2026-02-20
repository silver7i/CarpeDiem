#[S/W 문제해결 기본] 2일차 - Ladder1


for _ in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
     
    # 2 찾기
    for i in range(100):
        if arr[99][i] == 2:
            arr[99][i] = 0
 
            st_x = 99
            st_y = i
 
            while st_x > 0:
                # 좌
                if st_y > 0 and arr[st_x][st_y-1] == 1:
                    arr[st_x][st_y-1] = 0
                    st_y = st_y-1
                # 우
                elif st_y < 99 and arr[st_x][st_y+1] == 1:
                    arr[st_x][st_y+1] = 0
                    st_y = st_y+1
                # 위
                elif arr[st_x-1][st_y] == 1:
                    arr[st_x-1][st_y] = 0
                    st_x = st_x-1
 
             
 
     
            print(f'#{T} {st_y}')