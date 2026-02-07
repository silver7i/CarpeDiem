import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            return 0
    return 1
            

T = int(input())
for test_case in range(1, T + 1):
    word = input().strip()

    print(f'#{test_case} {is_palindrome(word)}')
