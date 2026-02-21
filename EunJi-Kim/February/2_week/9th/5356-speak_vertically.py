import sys
from pathlib import Path

file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)

sys.stdin = open(file_path, "r")

##############################

T = int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]

    stack = ['' for _ in range(15)]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            stack[j] += arr[i][j]

    print(f'#{tc}', ''.join(stack))
