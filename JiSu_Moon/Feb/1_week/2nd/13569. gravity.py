# gravity 


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_down = 0

    for i in range(N):  # 기준
        down = 0
        for j in range(i+1, N):  # 기준부터 오른쪽에 있는 박스
            if arr[i] > arr[j]:  # 오른쪽보다 기준이 크다면
                down += 1  # 낙차
        if down > max_down:  # 낙차중에 max 값 찾기
            max_down = down

    print(f'#{tc} {max_down}')