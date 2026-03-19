def backtrack():
    if len(ans) == M:
        print(*ans)
        return
    
    for i in range(N):
        if not p[i]:
            ans.append(arr[i])
            p[i] = True
            backtrack()
            ans.pop()
            p[i] = False
    

N, M = map(int, input().split())

arr = [num for num in range(1, N+1)]

p = [False] * N

ans = []

backtrack()