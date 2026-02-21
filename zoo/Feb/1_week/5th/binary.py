T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    book = [0] + list(range(1, P+1))

    start = 1
    end = P

    a_count = 0
    while start <= end:
        middle = int((start + end) // 2)
        if book[middle] == Pa:
            a_count += 1
            break
        elif book[middle] > Pa:
            end = middle
            a_count += 1
        else:
            start = middle
            a_count += 1

    start = 1
    end = P

    b_count = 0
    while start <= end:
        middle = int((start + end) // 2)
        if book[middle] == Pb:
            b_count += 1
            break
        elif book[middle] > Pb:
            end = middle
            b_count += 1
        else:
            start = middle
            b_count += 1


    if a_count > b_count:
        print(f"#{tc} B")
    elif a_count == b_count:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} A")
