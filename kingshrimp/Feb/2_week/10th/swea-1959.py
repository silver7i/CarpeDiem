# swea 1959
# ====
# 문제 아이디어
# 1. A, B 중에 뭐가 긴지 체크하기
# 2. 짧은것을 긴쪽에 따라서 한칸씩 이동을 하면서 서로의 값 맞추기
#     1. 앞에 빈 공백을 넣어서 맞추기
#     2. 인덱스 값의 차이를 넣어서 맞추기
# 값의 합 구하기
#     1. sum()을 사용하여 구하기
#     2. for문을 사용해서 최댓값 갱신 -> 두가지 이상 조건 구할때 사용 예)
# ===
import sys

sys.stdin = open('swea-1959i.txt')

def solve():
    A, B = map(int,input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    total = 0
    max_total = 0

    if A < B:
        long_list = list_b
        short_list = list_a
    else:
        long_list = list_a
        short_list = list_b
    # short_list로 돌리는게 나은지 long_list로 돌리는게 나은지 생각해보기
    for i in range(len(long_list)-len(short_list)+1):
        # total이라는 값의 초기값을 맨위에서 정할 필요는 없다.
        total = 0
        for j in range(len(short_list)):
            total += short_list[j] * long_list[i+j]
        if total > max_total:
            max_total = total
    
    return(max_total)

T = int(input())

for tc in range(1, T+1):
    res = (solve())
    print(f'#{tc} {res}')