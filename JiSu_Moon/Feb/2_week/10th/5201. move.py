# [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int,input().split()))
    Z = list(map(int,input().split()))

    # 내림차순 정렬
    w = sorted(W, reverse=True)
    z = sorted(Z, reverse=True)
    total = 0
    st = 0

    for i in range(M):  # 트럭 수
        flag = 0
        for j in range(st, N):  # 컨테이너 수, 옮긴 다음 화물부터
            if z[i] >= w[j]:
                flag = 1
                st = j+1
                total += w[j]
                break
        if flag == 0:
            break

    print(f'#{tc} {total}')