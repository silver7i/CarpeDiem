# [문제] 파리 퇴치 (2차원 배열, 완전 탐색, 구간 합)

# 1. 테스트 케이스 개수 입력
T = int(input())

for tc in range(1, T + 1):
    # 2. N(배열 크기), M(파리채 크기) 입력
    N, M = map(int, input().split())
    
    # 3. N x N 격자 입력 받기
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 4. 최댓값 담을 변수 초기화
    max_kill = 0 
    
    # 5. 파리채의 '왼쪽 위 모서리' 기준으로 전체 순회
    # 파리채가 배열 밖으로 나가지 않도록 범위 설정 (N - M + 1)
    for r in range(N - M + 1):      # 행(Row) 기준 이동
        for c in range(N - M + 1):  # 열(Col) 기준 이동
            
            # 6. 해당 위치에서 파리채 크기(M x M)만큼 합 구하기
            current_kill = 0
            for dr in range(M):     # 파리채 세로
                for dc in range(M): # 파리채 가로
                    current_kill += grid[r + dr][c + dc]
            
            # 7. 최댓값 갱신
            max_kill = max(max_kill, current_kill)
    
    # 8. 정답 출력
    print(f"#{tc} {max_kill}")