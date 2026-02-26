T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[] for _ in range(E+2)]

    for i in range(0, len(lst), 2):
        arr[lst[i]].append(lst[i+1])
    
    def abc(n):
        count = 1
        for i in arr[n]:
            count += abc(i)
        return count

    print(f'#{tc} {abc(N)}')