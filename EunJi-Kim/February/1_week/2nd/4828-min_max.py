import sys
sys.stdin = open("./input_src/4828-min_max.txt")


T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))

    max_num = arr[0]
    min_num = arr[0]

    for i in range(1, N):
        if max_num < arr[i]:
            max_num = arr[i]

        if min_num > arr[i]:
            min_num = arr[i]

    print(f'#{test_case} {max_num - min_num}')
