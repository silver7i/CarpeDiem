import sys
from pathlib import Path
from pprint import pprint

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################
'''
def is_palindrome(arr, target_len, index):    
    for i in range(target_len//2):
        if arr[index+i] != arr[index + target_len-1 -i]:
            return False, []

    return True, arr[index:index+target_len]


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    arr_col = ["".join(x) for x in zip(*arr)]

    # 회문이 있으면 시작 인덱스 저장해서 단어 추출할 예정
    palindrome_word = []
    is_palin = False

    for i in range(N):
        for j in range(N-M+1):
            # 행 검사
            is_palin, temp_arr = is_palindrome(arr[i], M, j)

            # 행에 있다면 검사 중지   
            if is_palin:
                palindrome_word.append(temp_arr)
                break
            # 없다면 열 검사
            else:
                is_palin, temp_arr = is_palindrome(arr_col[i], M, j)
                
                if is_palin:
                    palindrome_word.append(temp_arr)
                    break
        if is_palin:
            break

    print(f'#{test_case}', *palindrome_word)
'''
# 함수화

def is_palindrome(arr, target_len, index):    
    for i in range(target_len//2):
        if arr[index+i] != arr[index + target_len-1 -i]:
            return False

    return True

def check_palindrome(arr, find_len):
    arr_col = ["".join(x) for x in zip(*arr)]

    for i in range(len(arr)):
        for j in range(len(arr)-find_len+1):
            # 행 검사
            is_palin = is_palindrome(arr[i], find_len, j)

            # 행에 있다면 검사 중지   
            if is_palin:
                return arr[i][j:j+find_len]
            # 없다면 열 검사
            else:
                is_palin = is_palindrome(arr_col[i], M, j)
                
                if is_palin:
                    return arr_col[i][j:j+find_len]
    return []


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print(f'#{test_case}', check_palindrome(arr, M))