T = int(input())

for tc in range(1, T+1):
    N = int(input())
    zero = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for y in range(r1, r2+1):
            for x in range(c1, c2+1):
                zero[y][x] += 1
    
    count = 0
    for y in range(10):
        for x in range(10):
            if zero[y][x] == 2:
                count += 1
    
    # for _ in range(N):
    #     r1, c1, r2, c2, color = map(int, input().split())
    #     if color == 1:
    #         for y in range(r1, r2+1):
    #             for x in range(c1, c2+1):
    #                 if zero[y][x] == 0:
    #                     zero[y][x] = 1
    #                 if zero[y][x] == 2:
    #                     zero[y][x] = 3
        
    #     if color == 2:
    #         for y in range(r1, r2+1):
    #             for x in range(c1, c2+1):
    #                 if zero[y][x] == 0:
    #                     zero[y][x] = 2
    #                 if zero[y][x] == 1:
    #                     zero[y][x] = 3

    # count = 0
    # for y in range(10):
    #     for x in range(10):
    #         if zero[y][x] == 3:
    #             count += 1
    
    print(count)




    # print(count)