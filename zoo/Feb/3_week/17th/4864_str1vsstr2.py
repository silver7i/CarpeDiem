T = int(input())

for tc in range(1, T + 1):
    # 길이가 n인 target (작은 놈)
    target_str = input()
    # 길이가 m인 search (큰 놈)
    search_str = input()
    
    n = len(target_str)
    m = len(search_str)
    
    answer = 0
    
    # [수정 1] 긴 길이(m)에서 짧은 길이(n)를 빼야 합니다!
    # 범위: "전체 텍스트 길이" - "패턴 길이" + 1
    for i in range(m - n + 1):
        
        # [수정 2] if문 끝에 콜론(:) 추가
        # search_str(큰 놈)을 잘라서 target_str(작은 놈)과 비교
        if search_str[i : i + n] == target_str:
            answer = 1
            break
    
    print(f"#{tc} {answer}")