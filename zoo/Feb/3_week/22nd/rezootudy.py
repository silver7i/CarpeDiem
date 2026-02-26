n = int(input())

arr = list(map(int, input().split()))

# 출력 -> 중복하여 등장x 중 최댓값. 그런 원소 없다면 -1

max_val = -1

for num in arr:
    if max_val <= num:
        cnt = 0
        for elem in arr:
            if elem == num:
                cnt += 1
        if cnt == 1:
            max_val = num

print(max_val)