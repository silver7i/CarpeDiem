# # # # # # # # lebros = "LEBROS"

# # # # # # # # arr_lebros = [letter for letter in lebros]

# # # # # # # # check_letter = input()

# # # # # # # # answer = "None"
# # # # # # # # for i in range(len(arr_lebros)):    
# # # # # # # #     if arr_lebros[i] == check_letter:
# # # # # # # #         answer = i

# # # # # # # # print(answer)


# # # # # # # n, m = map(int, input().split())

# # # # # # # check_arr = list(map(int, input().split()))

# # # # # # # cnt = 0
# # # # # # # for num in check_arr:
# # # # # # #     if num == m:
# # # # # # #         cnt += 1

# # # # # # # print(cnt)


# # # # # # """
# # # # # # n개의 원소, q개의 질의
# # # # # # 1. 질의의 종류
# # # # # # - "1 a" a 번째 원소 출력
# # # # # # - "2 b" b 원소 찾아서 idx+1 출력, 없으면 0을 출력
# # # # # # - "3 s e" s 번째 원소부터 e 번째 원소까지 각 원소의 값을 공백 구분 차례대로 출력

# # # # # # 2. 목표
# # # # # # 각 질의를 차례대로 수행하는 프로그램 작성
# # # # # # """

# # # # # # n, q = map(int, input().split())

# # # # # # arr = list(map(int, input().split()))

# # # # # # for _ in range(q):
# # # # # #     request = list(map(int, input().split()))

# # # # # #     if request[0] == 1:
# # # # # #         print(arr[request[1]-1])

# # # # # #     elif request[0] == 2:
# # # # # #         idx = 0
# # # # # #         for i in range(n):
# # # # # #             if arr[i] == request[1]:
# # # # # #                 idx = i
# # # # # #                 idx += 1 # ~번째 원소
# # # # # #                 break # 제일 작은 원소의 것
# # # # # #         print(idx)

# # # # # #     else:
# # # # # #         for num in arr[request[1]-1 : request[2]]:
# # # # # #             print(num, end=' ')
# # # # # #         print()


# # # # # """
# # # # # A_num_arr: check
# # # # # B_num_arr: target

# # # # # B가 A의 연속 부분 수열이라면 "Yes" 아니라면 "No"
# # # # # """

# # # # # a, b = map(int, input().split())

# # # # # a_num_arr = ''.join(list(input().split()))
# # # # # b_num_arr = ''.join(list(input().split()))

# # # # # if b_num_arr in a_num_arr:
# # # # #     print("Yes")
# # # # # else:
# # # # #     print("No")


# # # # n = int(input())

# # # # arr = list(map(int, input().split()))

# # # # two_cnt = 0

# # # # for i in range(n):
# # # #     if arr[i] == 2:
# # # #         two_cnt += 1

# # # #     if two_cnt == 3:
# # # #         print(i+1)
# # # #         break


# # # arr = list(map(int, input().split()))

# # # max_val = 0

# # # for num in arr:
# # #     if max_val < num:
# # #         max_val = num

# # # print(max_val)


# # n = int(input())
# # arr = list(map(int, input().split()))

# # cnt = 0
# # min_val = arr[0]
# # for num in arr:
# #     if min_val > num:
# #         min_val = num

# # for num in arr:
# #     if num == min_val:
# #         cnt+=1

# # print(f"{min_val} {cnt}")


# arr = list(map(int, input().split()))

# min_val = 1000
# max_val = -1000
# for num in arr:
#     if num == 999 or num == -999:
#         break
#     elif num < min_val:
#         min_val = num
#     elif num >= max_val:
#         max_val = num

# print(max_val, min_val)


n = int(input())
a = list(map(int, input().split()))



a.sort()
a.reverse()

print(a[0], a[1])