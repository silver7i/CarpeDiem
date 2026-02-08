# 숫자 카드


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 카드 장수 N
    arr = list(map(int, input()))
    bucket = [0] * 10

    for i in arr:  # DAT 구하기
        bucket[i] += 1  # 카드 장수

    Max_number = 0
    Max_count = 0
    for j in range(len(bucket) - 1, -1, -1):  # 큰 수부터 탐색
        if bucket[j] > Max_count:
            Max_number = j  # 가장 많은 카드에 적힌 숫자
            Max_count = bucket[j]  # 카드 장수

    print(f'#{tc} {Max_number} {Max_count}')