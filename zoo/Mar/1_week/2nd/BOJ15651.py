def backtrack():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        ans.append(arr[i])
        backtrack()
        ans.pop()

N, M = map(int, input().split())

arr = [num for num in range(1, N+1)]

ans = []

backtrack()