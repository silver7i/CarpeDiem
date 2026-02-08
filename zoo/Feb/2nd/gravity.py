T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    max_cnt = 0
 
    for n in range(N-1):
        cnt = 0
 
        for i in range(n+1, N):
 
            if arr[n] > arr[i]:
                cnt += 1
 
            if max_cnt < cnt:
                max_cnt = cnt
 
    print(f"#{tc} {max_cnt}")