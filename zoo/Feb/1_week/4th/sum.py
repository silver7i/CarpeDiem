for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
 
    box = []
 
    for y in range(100):
        y_sum_box = 0
        for x in range(100):
            y_sum_box += arr[y][x]
        box.append(y_sum_box)
 
    for x in range(100):
        x_sum_box = 0
        for y in range(100):
            x_sum_box += arr[y][x]
        box.append(x_sum_box)
 
    i_sum_box = 0
    for i in range(100):
        i_sum_box += arr[i][i]
    box.append(i_sum_box)
 
    j_sum_box = 0
    for j in range(100):
        j_sum_box += arr[j][99-j]
    box.append(j_sum_box)
 
    print(f"#{n} {max(box)}")