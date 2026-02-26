# # # """
# # # 첫번째 최댓값 위치 찾기
# # # 그보다 왼쪽 최댓값 위치 찾기
# # # 그보다 왼쪽 최댓값 위치 찾기
# # # 이를 반복..
# # # 첫 번째 원소가 뽑히게 되면 이 과정 종료.

# # # 출력 : 최댓값 위치들( 첫번째 원소가 뽑히게 되면 = 1이 출력되면 끝)
# # # """

# # # n = int(input())

# # # a = list(map(int, input().split()))

# # # idx = n

# # # while idx >= 1:
# # #     max_num = 0
# # #     for i in range(idx):
# # #         if max_num < a[i]:
# # #             max_num = a[i]
# # #             idx = i
    
# # #     print(idx + 1, end = " ")


# # nums = list(map(int, input().split()))

# # max_num = 0
# # min_num = 1001

# # for num in nums:
# #     if max_num < num and num < 500:
# #         max_num = num
# #     if min_num > num and num > 500:
# #         min_num = num

# # print(max_num, min_num)


# n = int(input())
# price = list(map(int, input().split()))

# max_profit = 0

# for i in range(n-1):
#     for j in range(i+1, n):
#         if max_profit < price[j] - price[i]:
#             max_profit = price[j] - price[i]

# print(max_profit)

n = int(input())
nums = list(map(int, input().split()))

min_diff = 100
for i in range(n-1):
    for j in range(i+1, n):
        if min_diff > nums[j] - nums[i]:
            min_diff = nums[j] - nums[i]
print(min_diff)