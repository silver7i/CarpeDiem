import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################

T = int(input())
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    elec_station = list(map(int, input().split()))

    bus_station = [0] * (N + 1 + K)
    for i in range(M):
        bus_station[elec_station[i]] += 1

    # N 종점까지 가면서
    # k 만큼만 갈 수 있는데
    # 충전할 수 있으면 k 갱신됨.
    # 근데 최소로 충전해야 하니까
    # k 길이 안에 충전할 수 있는게 있으면 가장 먼 곳에서 충전

    far_elec = 0
    move_cnt = K
    charge_cnt = 0
    i = 1
    result = 1
    while i < N+1:
        if move_cnt < 1:
            break

        for j in range(move_cnt-1, 0, -1):      # j = 0, 1, 2 .. k-1
            if bus_station[i+j] == 1:
                far_elec = i+j
                break
            else:
                far_elec = 0

        if far_elec != 0:
            move_cnt -= (far_elec - i)
            move_cnt += K
            charge_cnt += 1
            
            i = far_elec

        elif far_elec == 0 and i < N or move_cnt <= 0:
            result = 0
            break

    if K < 1:
        print(f'#{test_case} {result}')
    else:
        print(f'#{test_case} {charge_cnt}')
