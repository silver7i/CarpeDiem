# 전기버스


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())  # [3, 10, 5]
    bus_stop = list(map(int, input().split()))  # [1, 3, 5, 7, 9]

    bus = 0  # 버스 위치
    count = 0  # 충전횟수

    while bus+K < N:  # 종점 도착 전까지
        flag = 0
        for j in range(K, 0, -1):  # 갈 수 있는 최대거리에서 가까운 충전소
            if bus+j in bus_stop:  # 정류장에 충전기가 있다면
                flag = 1
                count += 1  # 충전 횟수 더하기
                bus += j  # 버스 위치 갱신
                break
        if flag == 0:
            count = 0
            break


    print(f'#{tc} {count}')