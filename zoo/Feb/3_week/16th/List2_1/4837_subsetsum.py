t = int(input())

a_set = list(range(1, 13)) # 1~12까지 숫자를 원소로 가진 집합 a

for tc in range(1, t+1):
    # n 부분집합 원소 수, k 부분집합 합
    n, k = map(int, input().split())

    # 출력 -> n개 원소, 합이 k 부분집합의 수. 없으면 0
    answer = 0

    for i in range(1 << 12): # 0 ~ 2^12-1 까지 돎
        temp_sum = 0 # 일시적으로 사용할 부분집합 합 바구니
        temp_cnt = 0 # 일시적으로 사용할 부분집합 원소 수 바구니

        for j in range(12): # 0 ~ 11 까지 켜져 있는지 보기위해?
            if i & (1 << j): # 모든 부분집합 만들기
                temp_sum += a_set[j]
                temp_cnt += 1
        
        # 만들 때마다 조건 만족하는지 확인
        if temp_sum == k and temp_cnt == n:
            answer += 1 # 조건 만족시 개수 +1

    print(f"#{tc} {answer}")