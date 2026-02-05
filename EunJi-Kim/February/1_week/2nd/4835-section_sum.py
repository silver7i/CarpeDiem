import sys
sys.stdin = open("./input_src/4835-section_sum.txt")


# N개의 정수 배열 / 이웃한 M개의 합 계산
# M개의 합이 가장 큰 경우와 / 가장 작은 경우 차이 출력

# M개의 합이 큰 변수
# M개의 합이 작은 변수
# 배열, 인덱스 0부터 N-M+1개 만큼 돌림
# N=5, M=2 이면, range(4) [0, 1, 2, 3]
    # 돌리면서 M번 만큼 또 돌림
        # 돌면서 합을 구함
    # 만약에 max보다 크거나 min보다 작으면 바꿈

    # 차이 출력

T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_max = 0
    sum_min = 0

    # 전체 범위에서 마지막 구간의 첫번째 요소까지만 돌기
    for i in range(N - M + 1):
        # 각 구간의 합은 0으로 초기화해서 시작
        sum = 0
        # 합할 M개만큼 돌기
        for j in range(M):
            sum += arr[i + j]
            
        if sum > sum_max or sum_max == 0:
            sum_max = sum

        if sum < sum_min or sum_min == 0:
            sum_min = sum

    print(f'#{test_case} {sum_max - sum_min}')
