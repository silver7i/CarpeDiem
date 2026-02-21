for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 역방향 시작점 찾기
    for x in range(100):
        if ladder[99][x] == 2:
            # 역시작점 inv_start
            inv_start = x
            break # for x 탈출
    
    # 사다리 타기 시작 y = 99출발 ~ 0도착
    y = 99
    
    while y > 0: # y가 0에 도착하면 끝낼 거임
        # 왼쪽으로 가는 경우, 왼쪽에 1이 있음
        # 범위는 늘 고려하기
        if (0 <= inv_start - 1) and ladder[y][inv_start - 1] == 1:
            # 왼쪽에 1이 있는 만큼 갈거야
            while (0 <= inv_start - 1) and ladder[y][inv_start - 1] != 0:
                inv_start -= 1
        
        # 오른쪽으로 가는 경우, 오른쪽에 1이 있음
        # 범위는 늘 고려하기
        elif (inv_start + 1 <= 99) and ladder[y][inv_start + 1] == 1:
            # 오른쪽에 1이 있는 만큼 갈거야
            while (inv_start + 1 <= 99) and ladder[y][inv_start + 1] != 0:
                inv_start += 1
        
        # 위로 가기(+ while 끝내야지)
        y -= 1
        
        
    print(f"#{tc} {inv_start}")