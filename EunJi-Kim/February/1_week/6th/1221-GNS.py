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
    case_num, case_len = map(str, input().split())
    arr = list(map(str, input().split()))

    num_dict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}

    # 개수 세기
    count_arr = [0 for _ in range(len(num_dict))]
    for i in arr:   # 입력 배열을 돌면서 단어를 뽑아서
        count_arr[num_dict[i]] += 1     # num_dict에서 뽑아온 단어의 값을 찾아서 인덱스화하고 자리값 증가

    # 누적합
    for i in range(1, len(num_dict)):
        count_arr[i] += count_arr[i-1]

    # 정렬
    sorted_arr = [0 for _ in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):           # 입력된 배열을 순회하면서
        # count 한 배열에서 찾아서 자리에 배치
        count_arr[num_dict[arr[i]]] -= 1    # count_arr[0, 1, ... 값 찾음] 의 요소값 줄여감
        sorted_arr[count_arr[num_dict[arr[i]]]] = arr[i] # sorted_arr의 인덱스에 해당하는 자리에 넣기
    print(case_num, *sorted_arr)