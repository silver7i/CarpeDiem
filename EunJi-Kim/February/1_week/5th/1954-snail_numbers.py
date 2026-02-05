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
    N = int(input())

    # 오른쪽을 보면서 가다가 끝을 만나면
    # 시계방향대로 다음 방향을 보고
    # 있으면 가고
    # 가다가 없으면 다시 돌고 돌고 돌고
    arr = [[0 for _ in range(N)] for _ in range(N)]

    di = [0, 1, 0, -1]  # i 동남서북
    dj = [1, 0, -1, 0]  # j
    direction = 0

    now_i = 0
    now_j = 0
    # while 조건을 뭐로 줘야할까??
    # 계속 돌면서 다음을 찾음
    for i in range(N**2):
        # 현재 위치에 값 넣기
        arr[now_i][now_j] = i + 1
        # 지금 위치에 델타값을 더했을때 범위 안쪽이면 다음이 있음
        # and 다음 위치의 요소가 0이면 안갔던 곳임
        if now_i + di[direction] < N and now_j + dj[direction] < N \
                and arr[now_i + di[direction]][now_j + dj[direction]] == 0:
            # 다음으로 갈 위치를 변경
            now_i += di[direction]
            now_j += dj[direction]
        # 범위 밖이면 다음이 없으면
        else:
            # 방향 바꿈
            direction = (direction + 1) % 4     # direction : 0, 1, 2, 3
            # 다음으로 갈 위치를 변경
            now_i += di[direction]
            now_j += dj[direction]

    print(f'#{test_case}')
    for i in arr:
        print(*i)
