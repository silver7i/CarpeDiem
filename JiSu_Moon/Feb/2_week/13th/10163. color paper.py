# 색종이


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
arr = [[1]*1001 for _ in range(1001)]
result = []
for x in range(N-1, -1, -1):
    Sum = 0
    for i in range(paper[x][0], paper[x][0]+paper[x][2]):
        for j in range(paper[x][1], paper[x][1]+paper[x][3]):
            Sum += arr[i][j]
            arr[i][j] = 0
    result.append(Sum)

for y in range(N-1, -1, -1):
    print(result[y])