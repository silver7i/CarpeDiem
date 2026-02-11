# 간단한 369게임


N = int(input())
arr=[]

for i in range(1, N+1):  # 숫자 1부터 N까지
    number = str(i)
    count = 0
    for n in number:  # 숫자를 하나씩 검사
        if n == '3' or n == '6' or n == '9':  # 3, 6, 9 개수 세기
            count += 1

    if count > 0:
        arr.append('-'*count)  # 3, 6, 9 만큼 - 출력
    else:
        arr.append(i)  # 없다면 숫자 출력


print(*arr)