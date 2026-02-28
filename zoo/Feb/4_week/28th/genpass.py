for _ in range(2):
    tc = int(input())
    arr = list(map(int, input().split()))

    # 출력: 마지막 암호 베열은 모두 한 자리수.
    is_zero = False

    while not is_zero:
        for i in range(1,6):
            curr_num = arr.pop(0)

            curr_num -= i

            if curr_num <= 0:
                curr_num = 0
                arr.append(curr_num)
                is_zero = True
                break
                

            arr.append(curr_num)

    
    print(f"#{tc}", *arr)