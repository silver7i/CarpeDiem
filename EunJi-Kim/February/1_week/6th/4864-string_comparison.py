import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    find = 0
    for i in range(len(str2) - len(str1) + 1):
        cnt = 0
        for j in range(len(str1)):      # 찾는 문자
            if str1[j] != str2[i+j]:
                break
            cnt += 1

        if cnt == len(str1):
            find = 1
            break

    result = 1 if find == 1 else 0

    print(f'#{test_case} {result}')