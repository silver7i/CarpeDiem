import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "z_input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


def check(row, prob):
    global max_result

    if prob < max_result:
        return

    if row == N:
        max_result = max(max_result, prob)
        return
    
    for col in range(N):
        if visited[col] or board[row][col] == 0:
            continue

        visited[col] = 1
        prob *= (board[row][col] / 100)
        check(row + 1, prob)
        prob /= (board[row][col] / 100)
        visited[col] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # i번째 사람 / j번의 일
    # 주어진 일 모두 성공할 확률 => 최댓값
    # 한 사람당 1개 = 행/열 중복 x
    # row 순회하면서 col check
    # col visited로 확인
    # 언제를 완료 조건으로 보면 좋을까... 
    # 리스트를 넘겨주면서 채우면서 길이 체크하자
    # 인자는 리스트 정도?
    # max는 global

    visited = [0] * N
    max_result = 0

    check(0, 1)

    print(f"#{tc} {(max_result * 100):.6f}")
