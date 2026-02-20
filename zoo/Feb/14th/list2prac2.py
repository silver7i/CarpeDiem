t = int(input())

for tc in range(1, t+1):
    n = int(input()) # 행렬 size
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # 출력 -> 모든 원소에 대한 이웃한 숫자와의 차의 절대값에 대한 총 합
    answer = 0 # 합을 담을 바구니 만들기

    for y in range(n):
        for x in range(n):
            a_ij = matrix[y][x] # 기준 원소 설정
            # 우 하 좌 상 (이웃으로 이동하기 위해)
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ny = y + dy # 열 이동
                nx = x + dx # 행 이동
                if 0 <= ny < n and 0 <= nx < n: # 인덱스 범위 설정
                    # 이웃한 원소들끼리 차의 절댓값 변수에 할당
                    diff_abs = abs(a_ij - matrix[ny][nx])
                    # 바구니에 담기
                    answer += diff_abs
    
    print(f"#{tc} {answer}")