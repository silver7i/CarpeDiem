# [문제] Summation (2차원 배열 최대 합 구하기)

# 1. 10개의 테스트 케이스 처리
for _ in range(10):
    tc = int(input()) # 테스트 케이스 번호
    
    # 2. 100x100 2차원 배열 입력
    grid = [list(map(int, input().split())) for _ in range(100)]
    
    # 최댓값을 저장할 변수 초기화
    max_sum = 0
    
    # 3. [행]의 합 구하기 (가로)
    for row in grid:
        # sum() 함수로 한 행의 합을 즉시 계산
        max_sum = max(max_sum, sum(row))
    
    # 4. [열]의 합 구하기 (세로)
    for x in range(100):
        col_sum = 0
        for y in range(100):
            col_sum += grid[y][x]
        max_sum = max(max_sum, col_sum)
    
    # 5. [대각선]의 합 구하기 (크로스)
    diag1 = 0 # 우하향
    diag2 = 0 # 좌하향
    
    for i in range(100):
        diag1 += grid[i][i]
        diag2 += grid[i][99 - i]
        
    # 대각선 합들도 최댓값 후보에 포함
    max_sum = max(max_sum, diag1, diag2)
    
    # 6. 정답 출력
    print(f"#{tc} {max_sum}")