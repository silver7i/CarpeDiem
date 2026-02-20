import sys
from pathlib import Path

file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)

sys.stdin = open(file_path, "r")

##############################

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    i = 0
    cnt = 0
    while i < len(A):
        '''
        if i+len(B) <= len(A) and A[i] == B[0]:
            for j in range(len(B)):
                if A[i+j] != B[j]:
                    break
            else:
                cnt += 1
                i += len(B)
                continue
        cnt += 1
        i += 1
        '''
        if A[i:i+len(B)] == B:
            cnt += 1
            i += len(B)
        else:
            cnt += 1
            i += 1
    print(f'#{tc}', cnt)
