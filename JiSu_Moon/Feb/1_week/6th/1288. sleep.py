# 새로운 불면증 치료법


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [0]*10
    k = 1

    while True:
        number = N*k  # kN번째 5 10 15 20..
        for i in str(number):
            arr[int(i)] = 1  # 숫자에 맞는 해당 인덱스 더하기

            count = 0
            for j in range(10):
                if arr[j] == 1:  # 모든 인덱스가 1
                    count += 1

        if count == 10:
            break
        else:
            k += 1

    print(f'#{tc} {number}')
