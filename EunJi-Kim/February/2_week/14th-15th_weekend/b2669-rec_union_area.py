import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)                      # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")


###############################


rect_arr = [list(map(int, input().split())) for _ in range(4)]   # [x,y, x,y]

# board = [[0]*100]*100  # 이렇게 하면 얕은복사 되나?!?!!?!
board = [[0]*100 for _ in range(100)]

cnt = 0
# 사각형을 하나씩 보기
for rect in rect_arr: 
    for i in range(rect[0], rect[2]):   # 사각형의 왼쪽 아래 x좌표부터 오른쪽 위 x좌표전까지(그러면 칸은 다 채워짐)
        for j in range(rect[1], rect[3]): # y기준 "
            if board[i][j] == 0:
                board[i][j] = 1
                cnt += board[i][j]

print(cnt)
    

