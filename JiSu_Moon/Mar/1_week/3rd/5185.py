# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수


T = int(input())

for tc in range(1, T+1):
    n, number = input().split()

    ans = ''
    for x in number:
        ans += format(int(x,16),'04b')

    print(f'#{tc} {ans}')