# 줄 세우기


N = int(input())
line = list(map(int, input().split()))

arr = [0]*N
for i in range(N):
    if line[i] == 0:
        arr[i] = i+1
    elif line[i] != 0:
        for j in range(N-1, i-line[i], -1):
            arr[j] = arr[j-1]
        arr[i-line[i]] = i+1

print(*arr)