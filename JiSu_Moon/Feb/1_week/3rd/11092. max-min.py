# 최대 최소의 간격


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    Max = arr[0]  # 최대값
    Max_idx = 0  # 최대값 인덱스
    for i in range(len(arr)):
        if arr[i] >= Max:  # 최대값이 여러개이면 마지막에 나온 수
            Max = arr[i]
            Max_idx = i

    Min = arr[0]  # 최소값
    Min_idx = 0  # 최소값 인덱스
    for j in range(len(arr)):
        if arr[j] < Min:  # 최소값이 여러개이면 처음 나온 수
            Min = arr[j]
            Min_idx = j


    result = abs(Max_idx - Min_idx)  # 절대값 함수 ads()
    print(f'#{tc} {result}')