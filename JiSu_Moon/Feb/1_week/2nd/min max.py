# min max


T = int(input())  # 테스트 케이스의 수
for tc in range(1, T+1):  # TC(테이스 케이스 번호)
    N = int(input())  # 양수의 개수
    arr = list(map(int, input().split()))  # N개의 양수
    max_v = arr[0]  # 초기값 설정
    min_v = arr[0]

    for i in range(N):
        if arr[i] > max_v:
            max_v = arr[i]  # 가장 큰 수
        elif arr[i] < min_v:
            min_v = arr[i]  # 가장 작은 수

    print(f'#{tc} {max_v - min_v}')