def backtrack(curr):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(curr, N):
        ans.append(arr[i])
        backtrack(i)
        ans.pop()
        

N, M = map(int, input().split())

arr = [num for num in range(1, N+1)]

ans = []

backtrack(0)