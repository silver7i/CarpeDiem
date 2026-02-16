for tc in range(1, 11): # 총 10개의 테스트 케이스
    limit = int(input()) # 덤프 횟수
    box = list(map(int, input().split()))  # 100개의 상자 높이
    
    for _ in range(limit):
        box.sort() # 매번 정렬해서 양 끝을 본다
        
        # 이미 평탄화가 끝났다면(차이가 1 이하) 중단
        if box[-1] - box[0] <= 1:
            break
        
        # 덤프 실행 (최고점 -1, 최저점 +1)
        box[-1] -= 1
        box[0] += 1
    
    # 마지막 덤프 후 순서가 섞였을 수 있으니 max, min을 쓰는 것이 안전함.    
    print(f"#{tc} {max(box) - min(box)}")