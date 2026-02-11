# 스위치 조작


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for i in range(N):
        if A[i] != B[i]:
            cnt += 1
            for j in range(N-i):
                if A[i+j] == 1:
                    A[i+j] = 0
                    continue
                if A[i+j] == 0:
                    A[i+j] = 1

    print(f'#{tc} {cnt}')