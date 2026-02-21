t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split()) # n 정수의 개수, m 구간의 개수
    ai = list(map(int, input().split())) # n개의 정수 리스트
    
    # 정수가 모두 양수라서 가능
    max_val = 0
    min_val = int(1e9)
    
    # 안전한 초기화_첫 번째 구간의 합을 초기값으로
    current_sum = sum(ai[0:m])
    max_val = current_sum
    min_val = current_sum
    
    
    for i in range(n-m+1): # i번 원소부터 n-m 원소까지
        s = sum(ai[i:i+m]) # i번 원소를 포함해서 m개까지 합해서 s에 할당
        
        max_val = max(max_val, s) # max_val와 s를 비교해서 큰 값을 max_val에 할당
        min_val = min(min_val, s) # min_val와 s를 비교해서 작은 값을 min_val에 할당
        
    print(f"#{tc} {max_val - min_val}")