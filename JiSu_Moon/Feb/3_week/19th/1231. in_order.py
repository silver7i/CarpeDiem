# [S/W 문제해결 기본] 9일차 - 중위순회


for tc in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    lst = [0]*(N+1)
    for i in range(N):
        lst[int(arr[i][0])] = arr[i][1]
 
    new = []
    def in_order(now):
        if now >= len(lst):
            return
        in_order(now * 2)
        new.append(lst[now])
        in_order(now * 2 + 1)
 
    in_order(1)
    print(f'#{tc} ', *new, sep='')