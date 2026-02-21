# ---
# 이게 왜 스택이지???
# ---

import sys

sys.stdin = open('ws-04i.txt')

def solve():
    A, B = map(int,input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    total = 0

    if len(list_a) < len(list_b):
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
            total += short_list[j] * long_list[i]
        max_total = total
        if total > max_total:
            max_total = total
    
    print(max_total)

T = int(input())
for tc in range(1, T+1):
    solve()