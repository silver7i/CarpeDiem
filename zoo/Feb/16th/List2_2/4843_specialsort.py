# [문제] 특별한 정렬 (정렬, 투 포인터 활용)

T = int(input())

for tc in range(1, T + 1):
    N = int(input()) # 정수의 개수
    ai = list(map(int, input().split())) # 리스트 입력
    
    # 1. 오름차순 정렬 (핵심: 양끝 값을 쉽게 찾기 위함)
    # 정렬 후 상태: [최솟값, ..., ..., 최댓값]
    ai.sort()
    
    # 2. 투 포인터 초기화
    left = 0           # 가장 작은 수 위치 (맨 앞)
    right = N - 1      # 가장 큰 수 위치 (맨 뒤)
    result = []        # 정답을 담을 바구니
    
    # 3. 10개 추출 (큰 수, 작은 수 5쌍)
    # N이 100이든 1000이든, 문제 조건에 따라 딱 5번만 돌면 됨
    for _ in range(5):
        # (1) 가장 큰 수 먼저 담기
        result.append(ai[right])
        right -= 1 # 포인터 안쪽으로 이동
        
        # (2) 가장 작은 수 나중에 담기
        result.append(ai[left])
        left += 1  # 포인터 안쪽으로 이동
        
    # 4. 정답 출력 (언패킹 * 사용하여 공백 구분 출력)
    # 쉼표 뒤에 공백을 제거하고 *result가 공백을 만들어주도록 함
    print(f"#{tc}", *result)