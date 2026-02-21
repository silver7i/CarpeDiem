t = int(input())

for tc in range(1, t+1):
    str1, str2 = input().split()

    answer = 0

    # 필요한 재료 준비
    str2_cnt = str1.count(str2)
    l1 = len(str1)
    l2 = len(str2)

    answer += str2_cnt
    answer += (l1 - (l2 * str2_cnt))
    
    print(f"#{tc} {answer}")