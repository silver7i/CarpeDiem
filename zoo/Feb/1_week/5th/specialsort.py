T = int(input())

for tc in range(1, T+1):
    n = int(input())
    l1 = list(map(int, input().split()))

    # min_idx = list(range(1, n+1, 2))
    # max_idx = list(range(0, n+1, 2))

    l1.sort()

    min_l1 = l1[:(n//2)]
    max_l1 = l1[-1:(n//2)-1:-1]

    #     answer[1] = min_l1[0]
    #     answer[3] = min_l1[1]
    #     answer[5] = min_idx[2]
    #     ...       = ...
    #     answer[n] = min_idx[(n//2)]
    answer = [0] * n

    for i in range(0, n//2):
        answer[i*2+1] = min_l1[i]



    for j in range(0, n//2):
        answer[j*2] = max_l1[j]

    print(f"#{tc}", *answer[:10])
