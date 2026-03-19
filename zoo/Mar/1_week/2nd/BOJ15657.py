def backtrack(curr):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(curr, N):
        ans.append(arr[i])
        backtrack(i)
        ans.pop()

N, M = map(int, input().split())

arr = list(map(int, input().split()))

ans = []

arr.sort()

backtrack(0)