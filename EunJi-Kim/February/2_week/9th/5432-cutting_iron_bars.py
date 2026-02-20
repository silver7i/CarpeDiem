import sys
from pathlib import Path

file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)

sys.stdin = open(file_path, "r")

##############################


T = int(input())
for tc in range(1, T+1):
    arr = input()

    # '(' 개수만큼 막대 개수 증가, ')' 만나면 막대 개수 차감
    # 중간에 '(' 만나면 잘린 막대기 수에 추가
    # '()' 만나면 잘린 막대기 수에 막대 개수만큼 누적
    bar_num = 0
    cutting_bar_num = 0

    for i in range(len(arr)):
        if arr[i] == '(' and arr[i+1] == ')':
            cutting_bar_num += bar_num
        elif arr[i] == '(' and arr[i+1] != ')':
            bar_num += 1
            cutting_bar_num += 1
        elif arr[i-1] != '(' and arr[i] == ')':
            bar_num -= 1

    print(f'#{tc}', cutting_bar_num) # 잘려진 쇠 막대기 총 수
