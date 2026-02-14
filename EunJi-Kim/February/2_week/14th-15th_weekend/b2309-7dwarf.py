import sys
from pathlib import Path

# 1. 파일 경로 설정 및 폴더/파일 자동 생성
file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True) 
sys.stdin = open(file_path, "r")

########################################

def check_dwarfs_height(arr, found_dwarfs):
    if len(found_dwarfs) == 7:
        if sum(found_dwarfs) == 100:
            return True
        else:
            return False
    
    for i in range(len(arr)):
        found_dwarfs.append(arr[i])
        if check_dwarfs_height(arr[i+1:], found_dwarfs):
            return True
        found_dwarfs.pop()
    return False


input_dwarfs = [int(input()) for _ in range(9)]

found_dwarfs = []

check_dwarfs_height(input_dwarfs, found_dwarfs)
found_dwarfs.sort()

for i in found_dwarfs:
    print(i)