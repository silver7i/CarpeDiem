import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True) 
sys.stdin = open(file_path, "r")

########################################

def get_gender_room_cnt(gender_num, max_in):
    # 올림 공식
    return (gender_num + max_in -1) // max_in

    '''
    cnt = 0
    # 가능 인원수 나눈 몫이 0보다 클때, 나머지가 있는지 없는지
    if gender_num // max_in > 0:
        cnt += (gender_num // max_in)
        if gender_num % max_in > 0:
            cnt += 1
    # 몫이 0일 때, 나머지가 있는지 없는지
    elif gender_num // max_in == 0:
        if gender_num % max_in > 0:
            cnt += 1
    return cnt
    '''


N, k = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)] # (여0 / 남1), 학년

# 학년 인덱스에서 (여,남)의 수 구하기
counts = [[0, 0] for _ in range(7)]

for gender, grade in students:
    counts[grade][gender] += 1

room_cnt = 0
for female, male in counts:
    room_cnt += get_gender_room_cnt(female, k)
    room_cnt += get_gender_room_cnt(male, k)
print(room_cnt)

