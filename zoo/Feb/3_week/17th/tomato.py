for tc in range(1, 11):
# for _ in range(1):
    # length 회문의 길이
    length = int(input())
    # 8 x 8 size 
    matrix = [list(input()) for _ in range(8)]

    # 출력 -> 찾은 회문의 개수
    cnt = 0

    # 가로 
    for y in range(8):
        # 범위 작은거 해보기
        for x in range(8-length+1):
            # 슬라이딩 윈도우 회문인지 확인
            if matrix[y][x : x+length] == matrix[y][x : x+length][::-1]:
                cnt += 1 # 맞으면 개수 +1
    
    # 세로
    for x in range(8):
        for y in range(8-length+1):
            basket = [] # 세로는 슬라이스 안된다고 들움.. 직접 추가
            for step in range(length):
                # 회문 길이만큼만 담아
                basket.append(matrix[y+step][x])
            # 한 기준 원소에서 회문 길이만큼 담은 바구니 확인    
            if basket == basket[::-1]:
                cnt += 1 # 회문이면 +1

    print(f"#{tc} {cnt}")