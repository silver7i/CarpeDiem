t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split()) # n 행렬 크기, m 스프레이 파워
    # n x n 행렬 만들기
    fly_matrix = [list(map(int, input().split())) for _ in range(n)]
    
    # 출력 -> + 스프레이 or x 스프레이 범위 합 중 최대값
    max_kill = 0 # 최대값 초기화
    
    # spray[0] + 모양, spray[1] x 모양
    spray = [[(0, 1), (1, 0), (0, -1), (-1, 0)],
	    		   [(-1, 1), (1, 1), (1, -1), (-1, -1)]]
    
    for y in range(n):
        for x in range(n):
            
            for dy_dx_list in spray:
                current_sum = fly_matrix[y][x] # 행렬 원소 위치 이동시 현재 합 초기화
                
                for dy, dx in dy_dx_list:
                
                    for power in range(1, m):
                        ny = y + dy * power
                        nx = x + dx * power
                        
                        if 0 <= ny < n and 0 <= nx < n:
                            current_sum += fly_matrix[ny][nx]
                        # 범위 밖으로 벗어나는 순간 안봄    
                        else:
                            break # for power 탈출
                            
            if max_kill < current_sum:
                max_kill = current_sum
                
    print(f"#{tc} {max_kill}")