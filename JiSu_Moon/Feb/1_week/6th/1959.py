import sys
sys.stdin=open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N <= M:
        Max = -21e8
        for i in range(M-N+1):  # B의 범위
            Sum = 0
            for j in range(N):  # A의 범위
                Sum += B[i+j]*A[j]
            if Sum > Max:
                Max = Sum

    if N > M:
        Max = -21e8
        for i in range(N-M+1):  # A의 범위
            Sum = 0
            for j in range(M):  # B의 범위
                Sum += A[i+j]*B[j]
            if Sum > Max:
                Max = Sum

    print(f'#{tc} {Max}')