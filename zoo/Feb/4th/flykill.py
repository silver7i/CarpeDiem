T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for y1 in range(N-M+1): # 행 순환
        for x1 in range(N-M+1): # 열 순환 
            sum = 0
            for y2 in range(y1, y1+M):
                for x2 in range(x1, x1+M):
                    sum += arr[y2][x2]
            if answer < sum:
                answer = sum
    
    print(f"#{tc} {answer}")