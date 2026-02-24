for _ in range(4):
    arr = list(map(int, input().split()))

    print(sum(arr))


n = 4
arr_2d = []
for _ in range(n):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

print(arr_2d)

# >> 출력 결과
# [[1, 2, 3, 4], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]


n = 4
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
]
print(arr_2d)

# >> 출력 결과
# [[1, 2, 3, 4], [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]]
