import sys
from pathlib import Path
file_name = Path(__file__).stem
sys.stdin = open(f"./input_src/{file_name}.txt")


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # 가장 왼쪽의 인덱스가 낙차가 클 확률이 높음
    # 배열을 순회하면서
        # 자신보다 크거나 같은 요소를 찾은 개수대로 낙차 크기에서 뺌
    # 가장 큰 낙차값을 print

    max_drop = 0
    # 각 칸에 쌓인 높이 확인
    for i in range(N):
        # 나보다 높게 쌓인 (오른쪽) 상자 개수 기록
        cnt = 0
        #나보다 오른쪽 상자 살피기
        for j in range(i+1, N):
            # 나보다 높거나 같으면 개수 증가
            if num_list[i] <= num_list[j]:
                cnt += 1

        # 전체에서(N) - 자기자신(1) - 인덱스값(i) - 쌓인 블럭(cnt) 
        if max_drop < N - 1 - i - cnt:
            max_drop = N - 1 - i - cnt

    print(max_drop)