# 14158. 화물 도크


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        lst.append((s, e))
    lst.sort(key=lambda x: x[1])
 
    cnt = 0
    now = 0
    for s, e in lst:
        if now <= s:
            cnt += 1
            now = e
 
    print(f'#{tc} {cnt}')