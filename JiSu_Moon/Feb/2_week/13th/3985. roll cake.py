# 롤 케이크


L = int(input())
N = int(input())
I = [list(map(int, input().split())) for _ in range(N)]

Max = -21e8
Max_i = 0
for i in range(N):
    E = I[i][1]-I[i][0]
    if E > Max:
        Max = E
        Max_i = i+1
print(Max_i)

arr = [0] * L
for j in range(N):
    for x in range(I[j][0], I[j][1]+1):
        if arr[x-1] == 0:
            arr[x-1] = j+1
Max_r = -21e8
Max_r_idx = 0
for z in range(N):
    count = 0
    for box in arr:
        if box == z+1:
            count += 1
    if count > Max_r:
        Max_r = count
        Max_r_idx = z+1

print(Max_r_idx)

