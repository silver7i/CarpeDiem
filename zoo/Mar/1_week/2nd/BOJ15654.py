def backtrack():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        if not p[i]:
            p[i] = True
            ans.append(arr[i])
            backtrack()
            ans.pop()
            p[i] = False

N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

p =  [False] * N

ans = []

backtrack()