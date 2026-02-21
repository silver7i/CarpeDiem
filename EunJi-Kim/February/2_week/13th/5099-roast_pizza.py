import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)  # 파일이 없으면 생성

# 2. 파일 읽기 연동
sys.stdin = open(file_path, "r")

###############################


T = int(input())
for test_case in range(1, T+1): 
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    oven = [0] * (N)
    front = 0
    rear = -1

    # 피자 번호 받아오기 위한 이중배열
    Ci_dict = []
    for i in range(len(Ci)):
        Ci_dict.append([Ci[i], i+1])

    # 오븐 초기화
    while rear < N-1 and Ci_dict:
        rear += 1
        oven[rear] = Ci_dict.pop(0)
    
    result = -1
    while oven: # Ci에 아무것도 없고 front와 rear가 1차이 날 때 1개만 남아있는 것
        
        # 오븐 돌리기
        oven[front][0] //= 2

        if oven[front][0] == 0:
            result = oven[front][1]
            oven.pop(0)
            rear -= 1

            if Ci_dict:
                oven.append(Ci_dict.pop(0))
                rear += 1
        else:
            oven.append(oven[front])
            oven.pop(0)

    print(f'#{test_case} {result}')

        
