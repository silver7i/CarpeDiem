T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_n = list(map(int, input().split()))
    list_m = list(map(int, input().split()))
 
    for _ in range(N):
        pop_num = list_n.pop()
 
        if not list_m:
            break
 
        if list_m[-1] == pop_num:
            list_m.pop()
 
    if not list_m:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")