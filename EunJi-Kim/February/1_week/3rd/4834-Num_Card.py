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
    num = int(input())
    
    # 입력받은 숫자 쪼개서 count 배열에 개수만큼 저장
    count = [0] * 10
    for i in range(N):
        count[num % 10] += 1    # 10으로 나눈 나머지가 count의 인덱스가 되서 개수 증가
        num //= 10              # num 숫자 갱신

    max_num = 0
    for i in range(len(count)):     # count 배열 개수대로 돌면서
        if count[i] >= count[max_num]:  # 갖고있는 값(요소의 값)이 큰거 찾기
            max_num = i

    print(f'#{test_case} {max_num} {count[max_num]}')