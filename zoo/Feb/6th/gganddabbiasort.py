T = int(input())

for _ in range(1, T+1):
    tc, N = input().split()
    N = int(N)
    arr = list(input().split())

    gganddabbia = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    answer = []
    for gdb in gganddabbia:
        for i in range(N):
            if arr[i] == gdb:
                answer.append(gdb)
    print(f"{tc}")
    print(*answer)
