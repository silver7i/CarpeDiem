"""
5
1
2
11
1295
1692
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [-1] * 10

    i = 0
    now_num = N
    while -1 in arr:
        i += 1
        now_num = N * i
        for j in str(now_num):
            arr[int(j)] = int(j)
        
    print(f'#{tc} {now_num}')
    
        
