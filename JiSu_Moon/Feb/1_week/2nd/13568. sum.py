# 구간합


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input(). split()))  # 정수의 개수 N, 구간의 개수 M
    arr = list(map(int, input(). split())) # N개의 정수 배열
    max_v = 0
    min_v = 0
    for x in range(M):  # 최소값, 최대값 설정
        max_v += arr[x]
        min_v += arr[x]

    for i in range(N-M+1):  # 경우의 수
        Sum = 0
        for j in range(i, M+i): # i번 부터 M개의 합
            Sum += arr[j]
        if Sum > max_v:
            max_v = Sum
        elif Sum < min_v:
            min_v = Sum

    print(f'#{tc} {max_v - min_v}')