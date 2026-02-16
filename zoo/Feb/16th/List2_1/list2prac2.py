import sys
# input = sys.stdin.readline  # 입력 데이터가 많을 때 사용

T = int(input())

# 방향 벡터 (상, 하, 좌, 우) - 순서는 상관없음
# 미리 정의해두면 코드가 깔끔해짐
dr = [-1, 1, 0, 0] # 행 이동 (dy 대신 dr)
dc = [0, 0, -1, 1] # 열 이동 (dx 대신 dc)

for tc in range(1, T + 1):
    N = int(input())
    
    # 2차원 배열 입력 받기
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    total_sum = 0 # 전체 합

    # r: 행(row), c: 열(column)
    for r in range(N):
        for c in range(N):
            # 현재 위치의 값
            current_val = matrix[r][c]
            
            # 4방향 탐색
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                
                # 범위 체크 (0 <= nr < N and 0 <= nc < N)
                if 0 <= nr < N and 0 <= nc < N:
                    # 차이의 절댓값 더하기
                    total_sum += abs(current_val - matrix[nr][nc])
                    
    print(f"#{tc} {total_sum}")