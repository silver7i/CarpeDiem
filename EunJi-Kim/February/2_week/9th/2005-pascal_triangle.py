'''
1
6
'''


###############################

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    arr = [[1],]

    for i in range(1, N):
        inner_arr = []
        for j in range(i+1):
            sum_value = 0
            if 0 <= j-1:
                sum_value += arr[i-1][j-1]
            if  j < len(arr[i-1]):
                sum_value += arr[i-1][j]
            
            inner_arr.append(sum_value)
        arr.append(inner_arr)

    print(f'#{test_case}')
    for i in arr:
        print(*i)

