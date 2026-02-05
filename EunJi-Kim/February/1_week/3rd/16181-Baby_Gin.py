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
    # 0~9 arr
    nums = int(input())
    counts = [0] * 12   # 왜 12인가? 나란한 3자리를 비교할 때 9의 자리에서 10 , 11의 자리에 대한 예외처리를 안하려고

    # arr를 순회하면서
    # counts의 인덱스 자리의 번호가 arr의 데이터로 있으면 개수만큼 counts 인덱스 자리의 값을 증가
    for i in range(6):
        counts[nums % 10] += 1
        nums //= 10

    # 다시 counts를 순회하면서 3이상의 값이 있는지 확인
    # 있다면 3개 지움
    # 0보다 큰 값이 나란히 있는지 확인
    # 있다면 나란히 있던 값 run에 해당하는 값들을 1씩 지움

    i = 0
    tri_cnt = run_cnt = 0
    while(i < 10):
        if counts[i] >= 3:
            counts[i] -= 3
            tri_cnt += 1
            continue
        if counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            run_cnt += 1
            continue
        i += 1

    if run_cnt + tri_cnt == 2:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')