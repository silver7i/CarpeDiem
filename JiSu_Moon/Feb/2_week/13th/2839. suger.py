# 설탕 배달


N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += N//5
        N = 0
        break
    elif N >= 3:
        N = N-3
        cnt += 1
    elif N < 3:
        break

if N == 0:
    print(cnt)
else:
    print(-1)