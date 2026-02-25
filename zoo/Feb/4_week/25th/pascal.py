# [문제] 파스칼의 삼각형 (DP 기초)

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    tri = [] # 이전 행들의 정보를 기억할 공간
    
    print(f"#{tc}")
    
    for row in range(n):
        tri_row = [] # 현재 행을 담을 빈 리스트
        
        for column in range(row + 1):
            # 양 끝은 1
            if column == 0 or column == row:
                tri_row.append(1)
            # 중간 값은 왼쪽 위 + 오른쪽 위
            else:
                tri_row.append(tri[row-1][column-1] + tri[row-1][column])
                
        # 한 행이 완성되면 바로 출력하고, 전체 리스트에 보관
        print(*tri_row)
        tri.append(tri_row)