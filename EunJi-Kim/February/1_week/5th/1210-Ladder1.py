import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################



T = 10
for test_case in range(1, T + 1):
    t = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 당첨 위치가 시작 위치가 될거여서 북으로만 이동 / 남으로 가기위한 델타는 없어도 됨
    di = [0, 0, -1]  # 동서북
    dj = [1, -1, 0]
    direction = 0       # 0 1 2 = 오 왼 위

    now_i = N-1
    now_j = 0

    # 시작 위치를 구함
    for i in range(N):
        if arr[now_i][i] == 2:
            now_j = i
            break

    # 움직이고 있음을 알리는 변수
    move = 0
    while now_i > 0:
        # 왼쪽 오른쪽을 보면서 1을 찾음
        # 없으면 위로 이동

        # 오른쪽이 없으면 왼쪽 보고
        # 왼쪽도 없으면 위로 가
        # 좌/우로 가고 있었으면
        # 다음은 위로 가

        # 왼쪽 끝, 오른쪽 끝 범위 제한 두고, 1을 찾으면
        if now_i + di[direction] < N and now_j + dj[direction] < N \
                and now_i + di[direction] >= 0 and now_j + dj[direction] >= 0 \
                and arr[now_i + di[direction]][now_j + dj[direction]] == 1:
            # 다음 위치값 변경
            now_i += di[direction]
            now_j += dj[direction]
            move += 1

            # 위로 가던 중이면 멈춰서 좌우 확인 준비
            if direction == 2:
                direction = 0
                move = 0
        # 갈 곳이 없으면
        # 방향을 바꾸고 위치값 변경
        else:
            # 좌우를 확인할때 움직이지 않고 있었다면 좌로든 우로든 움직이지 않았다는 뜻
            if direction == direction % 2 and move == 0:
                direction = (direction + 1) % 3     # direction = 0, 1, 2
            # 좌우 어디든 움직이고 있었다면 위로 가도록
            elif direction == direction % 2 and move != 0:
                direction = 2

    print(f'#{t} {now_j}')