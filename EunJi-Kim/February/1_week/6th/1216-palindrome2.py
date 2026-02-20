import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def check_palind(arr):
    for l in range(len(arr)//2):
        if arr[l] != arr[len(arr)-1 - l]:
            return False
    return True

T = 10
for test_case in range(1, T + 1):
    t = int(input())
    N = 100
    arr = [input() for _ in range(N)]

    max_len = 0
    for i in range(N):                              # 행 검사
        for j in range(N):                          # 앞에서 짧아짐
            for k in range(N-1, 0, -1):             # 뒤에서 짧아짐
                if check_palind(arr[i][j:k+1]):
                    if k-j+1 > max_len:
                        max_len = k-j+1
                    break
    
    col_arr = [''.join(i) for i in zip(*arr)]
    for i in range(N):                              # 열 검사
        for j in range(N):                          # 앞에서 짧아짐
            for k in range(N-1, 0, -1):             # 뒤에서 짧아짐
                if check_palind(col_arr[i][j:k+1]):
                    if k-j+1 > max_len:
                        max_len = k-j+1
                    break
            
    print(f'#{t} {max_len}')



            
    
