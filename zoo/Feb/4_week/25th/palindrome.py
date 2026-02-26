# transpose 시킨다면

for tc in range(1, 11):
    N = int(input())
    
    # 1. 원본 글자판 (입력을 바로 문자열로 받음)
    board = [input().strip() for _ in range(8)]
    
    # 2. 90도 뒤집힌 글자판 만들기
    # zip(*board)가 세로줄을 뽑아주면, join으로 다시 문자열로 합침
    transposed_board = ["".join(col) for col in zip(*board)]
    
    cnt = 0
    
    # 3. 이중 반복문 하나로 가로/세로 동시 검사
    for i in range(8):
        for j in range(8 - N + 1):
            
            # 원본 판에서 가로로 자르기
            h_window = board[i][j : j+N]
            # 뒤집힌 판에서 가로로 자르기 (결과적으로 원본의 세로를 자른 것과 동일)
            v_window = transposed_board[i][j : j+N]
            
            # 가로 회문 검사
            if h_window == h_window[::-1]:
                cnt += 1
            # 세로 회문 검사
            if v_window == v_window[::-1]:
                cnt += 1
                
    print(f"#{tc} {cnt}")