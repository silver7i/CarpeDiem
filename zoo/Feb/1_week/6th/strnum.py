T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = input()

    max_ans = 0

    for s in str1:
        ans = 0
        for i in range(len(str2)):
            if str2[i] == s:
                ans += 1
        if max_ans < ans:
            max_ans = ans

    print(f"#{tc} {max_ans}")
