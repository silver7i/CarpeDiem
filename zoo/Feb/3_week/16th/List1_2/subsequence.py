t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split()) # n: A수열의 길이 , m: B수열의 길이
    a = list(map(int ,input().split())) # A수열
    b = list(map(int, input().split())) # B수열
    
    # 출력 -> B가 A의 부분 수열이면 YES 아니면 NO
    current_idx = 0 # 갱신할 인덱스 변수 할당
    
    cnt = 0 # cnt가 b 개수만큼 채워지면 YES 출력하기 위해서
    
    for target in b:
        
        flag = False # 스위치 설정
        
        for idx in range(current_idx, n):
            if a[idx] == target:
                cnt += 1
                idx = current_idx
                flag = True
                break
        
        if not flag: # 위에서 못찾으면(flag = True로 바뀌지 않으면) 더 볼 필요 없다.
            break
        
    if cnt == m:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")            