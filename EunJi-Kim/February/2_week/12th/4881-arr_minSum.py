import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################

def find_min_sum(arr, N, now_i, now_j, select_ij, min_sum):
    """
    :param arr: N*N 배열
    :param N: 고를 개수
    :param now_ij: 지금의 행,열 1차원 배열
    :param select_ij: 선택한 행, 열 2차원 배열
    :param min_sum: 최소 합
    """
    

   
    

T = int(input())
for test_case in range(1, T+1):  
    N = int(input())
    arr = [ list(map(int, input().split())) for _ in range(N)]
    
    print(find_min_sum(arr, N, 0, 0, [], 100))

    # 배열을 넘겨주고
    # 행 인덱스랑 열 인덱스 저장하는 배열 필요할거 같고
    # 지금 위치 필요할거 같고
    # 고를 개수 N
