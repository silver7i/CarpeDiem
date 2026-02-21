import sys
from pathlib import Path

file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)

sys.stdin = open(file_path, "r")

##############################

T = 10
for tc in range(1, T+1):
    N, nums = input().split()

    password = []
    for num in nums:
        if not password or password[-1] != num:
            password.append(num)
        elif password[-1] == num:
            password.pop()
    print(f'#{tc}', ''.join(password))