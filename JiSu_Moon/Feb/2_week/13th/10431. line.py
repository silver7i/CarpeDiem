# 줄세우기


P = int(input())
for x in range(P):
    line = list(map(int, input().split()))
    T = line.pop(0)
    cnt = 0

    for i in range(20-1, -1, -1):
        for j in range(i):
            if line[j] > line[j+1]:
                line[j], line[j+1] = line[j+1], line[j]
                cnt += 1

    print(T, cnt)