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
    str1 = set(input())
    str2 = input()

    str_dic = {}

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
                str_dic[i] = cnt
                
    print(f'#{test_case} {max(str_dic.values())}')

'''
    str_dic = {}
    max_cnt = 0
    for i in str1:
        if i in str_dic:
            continue

        for j in str2:
            if i == j:
                if i not in str_dic:
                    str_dic.setdefault(i, 1)
                else:
                    str_dic[i] += 1

        if str_dic[i] > max_cnt:
            max_cnt = str_dic[i]

    print(f'#{test_case} {max_cnt}')
'''
    