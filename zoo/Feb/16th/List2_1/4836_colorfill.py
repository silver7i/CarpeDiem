# 1. 테스트 케이스 개수 입력
T = int(input())

for tc in range(1, T + 1):
    # 2. 문제 조건 입력 (칠할 영역 개수 N)
    N = int(input())
    
    # 3. 격자판 초기화 (10x10)
    # [[0] * 열개수 for _ in range(행개수)]
    grid = [[0] * 10 for _ in range(10)]
    
    # 4. N번 반복하며 색칠하기 (명령 수행)
    for _ in range(N):
        # r1, c1: 시작 좌표 / r2, c2: 끝 좌표 / color: 색상
        r1, c1, r2, c2, color = map(int, input().split())
        
        # 5. 범위 순회하며 값 누적 (핵심 로직)
        # 끝 좌표까지 포함해야 하므로 +1 필수!
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                grid[r][c] += color  # 1(빨강) + 2(파랑) = 3(보라)
    
    # 6. 결과 계산 (조건에 맞는 칸 세기)
    answer = 0
    for r in range(10):
        for c in range(10):
            if grid[r][c] == 3:  # 보라색인 경우
                answer += 1
                
    # 7. 정답 출력
    print(f"#{tc} {answer}")