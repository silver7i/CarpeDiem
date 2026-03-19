def traversal(N):
    if N == 0:
        return 0
    else:
        l = traversal(c1[N])
        r = traversal(c2[N])
        return l + r + 1


t = int(input())
for tc in range(1, t+1):
    E, N = map(int, input().split())

    arr = list(map(int, input().split()))

    V = E + 1

    c1 = [0] * (V+1)
    c2 = [0] * (V+1)
    
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    ans = traversal(N)
    print(f"#{tc} {ans}")