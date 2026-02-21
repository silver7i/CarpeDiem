def binary_search(total_page, target):
    # l 시작 페이지, r 끝 페이지, c 중간 페이지
    l = 1
    r = total_page
    
    # cnt 횟수 바구니
    cnt = 0
    
    while l <= r:
        c = int((l+r)/2) # 중간 페이지 갱신
        cnt += 1 # 횟수 + 1
        
        if c > target: # 중간 페이지가 target 보다 크면 (왼쪽 검색)
            r = c # 오른쪽 페이지 갱신
        elif c < target: # 중간 페이지가 target 보다 작으면 (오른쪽 검색)
            l = c # 왼쪽 페이지 갱신
        else: # 중간 페이지가 target이랑 같아지면
            return cnt
    
    return cnt
    
t = int(input())

for tc in range(1, t+1):
    p, pa, pb = map(int, input().split())
    
    a_cnt = binary_search(p, pa)
    b_cnt = binary_search(p, pb)
    
    if a_cnt > b_cnt:
        result = "B"
    elif a_cnt < b_cnt:
        result = "A"
    else:
        result = "0"
    
    print(f"#{tc} {result}")