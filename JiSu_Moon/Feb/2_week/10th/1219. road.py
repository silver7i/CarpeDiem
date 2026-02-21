# [S/W 문제해결 기본] 4일차 - 길찾기


for _ in range(10):
    T, N = map(int, input().split())
    numbers = list(map(int, input().split()))
    arr = [[] for _ in range(100)]
    for x in range(0, len(numbers), 2):
        arr[numbers[x]].append(numbers[x+1])

    visited = [0]*100
    def dfs(n):
        visited[n] = 1

        for next in arr[n]:
            if visited[next] == 0:
                dfs(next)

    dfs(0)

    if visited[99]:
        print(f'#{T} 1')
    else:
        print(f'#{T} 0')