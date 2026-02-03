# [S/W 문제해결 기본] 1일차 - View


for tc in range(1, 11):
    N = int(input())  # 건물의 개수 N
    H = list(map(int, input().split()))  # 건물의 높이 H
    view = 0

    for i in range(2, N-2):  # 기준이 되는 건물
        max_h = 0
        for j in range(i-2, i+3):  # 좌우 2칸의 건물
            if i != j:  # 본인 제외
                if max_h < H[j]:
                    max_h = H[j]
        if H[i] > max_h:  # 음수면 더하지 않음
            view += H[i] - max_h  # 조망권 개수 더하기

    print(f'#{tc} {view}')