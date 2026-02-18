# 방 배정


N, K = map(int, input().split())
arr = [[0,0] for _ in range(6)]


for _ in range(N):
    S, Y = list(map(int, input().split()))
    if S == 0:  # 여학생
        for i in range(1, 7):
            if Y == i:
                arr[i-1][0] += 1
                break
    if S == 1:  # 남학생
        for j in range(1, 7):
            if Y == j:
                arr[j-1][1] += 1
                break

# 필요한 방개수
room = 0
for x in arr:
    for y in x:
        if y > 0:
            room += (y+K-1) // K

print(room)