t = int(input())

for tc in range(1, t+1):
    n = int(input()) # 가로 길이 ex. 9: 원소 9개, 인덱스 0~8까지
    box = list(map(int, input().split())) # 상자 높이
    
    max_drop = 0
    
    for i in range(n): # i번 원소를 고정시킨 채로
        cnt = 0 # cnt 초기화
        for j in range(i+1, n): # i+1~끝까지 / 자기 다음 거부터 비교하면 되니까
            if box[i] > box[j]: # 자기보다 작은 원소 만나면
                cnt += 1 # cnt에 1씩 더해
        
        max_drop = max(max_drop, cnt) # for j 문 다 돌면(cnt다 세면)  max_drop값이랑 cnt이랑 비교해서 max_drop 값 갱신
	      
    print(f"#{tc} {max_drop}")    
    