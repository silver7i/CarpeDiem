T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    # 인덱스 접근을 위해 리스트 유지, 도착지점 처리를 위해 N 추가하지 않아도 됨 (위치만 중요)
    chargers = list(map(int, input().split()))
    
    # 충전소 유무를 빠르게 확인하기 위한 배열 (0~N)
    # 0번 인덱스부터 N번 인덱스까지, 충전소면 True
    has_charger = [False] * (N + 1)
    for c in chargers:
        has_charger[c] = True

    pos = 0   # 현재 위치
    cnt = 0   # 충전 횟수
    
    while pos + K < N: # 현재 위치 + K가 N보다 작으면 계속 충전해야 함
        # 최대한 멀리(K) 점프해서 뒤로 오면서 충전소 찾기
        for move in range(K, 0, -1):
            if has_charger[pos + move]:
                pos += move
                cnt += 1
                break
        else:
            # for문이 break 없이 끝남 = 갈 수 있는 범위 내에 충전소가 없음
            cnt = 0
            break
            
    print(f"#{tc} {cnt}")