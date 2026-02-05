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

    move_cnt = K

    charge_cnt = 0
    now = 0
    while now + K < N:
        found_station = False
        for j in range(K, 0, -1):      # j = 0, 1, 2 .. k-1
            # 가장 먼 충전소를 발견하면 현재 위치를 옮김
            if bus_station[now+j] == 1:
                now = now+j
                    # 내 생각에는 움직일 수 있는 값이 남아있으면 추가로 k를 더하는 건줄 알았는데
                    # move_cnt 값 제어하는게 없어야 정답이 되는거면 그냥 '가득이요~' 하고 가득 채우는거였나봄....
                # move_cnt -= (far_elec - now)  
                # move_cnt += K                 
                charge_cnt += 1
                found_station = True
                break

        if not found_station:
            charge_cnt = 0
            break

    print(f'#{test_case} {charge_cnt}')
    
