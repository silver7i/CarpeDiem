for tc in range(1, 11): # 총 10개의 테스트케이스가 주어진다.
    n = int(input()) # 건물의 개수 n
    buildings = list(map(int, input().split())) # n개의 건물의 높이 리스트, 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0.
    
    # 출력 -> 조망권이 확보된 세대의 수
    total_view = 0 # 조망권 확보될 때마다 수를 더할 것임. 그 시작점 0
    
    for i in range(2, n-2): # 맨 왼쪽, 오른쪽 두칸은 모두 0이니 2~(n-3)원소까지만 체크
        neighbor_max = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]) # 내 주변 중 제일 큰것 값 할당
        
        if buildings[i] > neighbor_max: # 내가 주변 중 제일 크다면
            total_view += (buildings[i] - neighbor_max) # total_view에 그 차이(조망권 확보 세대의 수)만큼 더해줌
            
    print(f"#{tc} {total_view}")