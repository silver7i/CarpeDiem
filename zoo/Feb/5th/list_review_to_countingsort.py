# 배열 원소 중 최댓값 max_v 찾기
arr = [2, 7, 5, 3, 1, 4]

## 첫 원소의 값을 사용하여 첫 원소를 최대로 가정
max_v = arr[0]

## arr[i]가 더 크면 max_v 갱신
for i in range(1, len(arr)): # 인덱스 1~끝까지 돌면서
    if max_v < arr[i]: # 더 큰 값 만나면
        max_v = arr[i] # 그 값으로 갱신
print(max_v) #7


# 배열 원소 중 최댓값의 인덱스 max_idx 찾기
arr = [2, 7, 5, 3, 1, 4]

## 첫 원소의 인덱스를 사용하여 첫 원소를 최대로 가정
max_idx = 0

## arr[i]가 arr[max_idx]보다 크면 max_idx 갱신
for i in range(1, len(arr)): # 인덱스 1~끝가지 돌면서
    if arr[max_idx] < arr[i]: # 더 큰 값 만나면
        max_idx = i # 그 인덱스로 인덱스 갱신
print(max_idx) # 1


# 최댓값이 여러 개인 경우 마지막 인덱스 찾기
arr = [2, 7, 5, 3, 1, 7]

## 첫 원소의 인덱스를 사용하여 첫 원소를 최대로 가정
max_idx = 0

## arr[i]가 arr[max_idx]보다 크거나 같으면 max_idx 갱신
for i in range(1, len(arr)): # 인덱스 1~끝까지 돌면서
    if arr[max_idx] <= arr[i]: # 더 크거나 같은 값 만나면
        max_idx = i # 그 인덱스로 인덱스 갱신
print(max_idx) # 5


# 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1을 인덱스
arr = [2, 7, 5, 3, 1, 7]

## 찾는 값이 없다고 가정
idx = -1

## arr[i]가 찾는 값이면 idx 갱신
for i in range(len(arr)): # arr 0 ~ 끝까지 돌면서
    if arr[i] == 5: # 5일 때 찾아서
        idx = i # 그 때 인덱스를 idx로 갱신
        break # 즉시 탈출 -> 맨 처음 발견했을 때 탈출
print(idx) # 2


# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력
arr = [477162, 658880, 751280, 927930, 297191]

## 작은 수를 최대로 설정
max_val = 0

## 개 큰 수를 최소로 설정
min_val = int(1e9)

## 최댓값, 최솟값 갱신
for val in arr: # 리스트 원소를 돌면서
    if max_val < val:
        max_val = val
    if min_val > val:
        min_val = val
print(max_val - min_val)


# Gravity
box = [7, 4, 2, 0, 0, 6, 0, 7, 0]
"""

"""

## 작은 수를 최대로 설정
max_count = 0

## 최대 인덱스 차 갱신하기
for i in range(len(box)-1):
    ### 떨어지는 횟수 카운트
    fall_count = 1 # 본인 위치 포함
    for j in range(idx+1, len(box)):
        if box[i] >= box[j]:
            fall_count += 1
    if max_count < fall_count:
        max_count = fall_count

print(max_count) # 7


# 버블 정렬(오름차순)
arr = [55, 7, 78, 12, 42]
"""
0 -> 1 이랑 비교
1 -> 2 랑 비교
2 -> 3 랑 비교
3 -> 4 랑 비교
최대값 맨 우측으로 감.
0 -> 1 이랑 비교
1 -> 2 랑 비교
2 -> 3 랑 비교
그 다음으로 큰 값
...
"""
for i in range(len(arr)-1, 0, -1):
    for j in range(i): 
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)


# 카운팅 정렬
arr = [0, 4, 1, 3, 1, 2, 4, 1]

## DATA에서 각 항목들의 발생 횟수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열
counts = [0] * len(set(arr)) # [0, 0, 0, 0, 0]
"""
arr에서 0 -> counts[0] += 1
arr에서 4 -> counts[4] += 1
arr에서 1 -> counts[1] += 1
...
"""
for arr_val in arr:
    counts[arr_val] += 1
### counts = [1, 3, 1, 1, 2]

## 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts 원소 조정
"""
0 + 1 = 1
1 + 2 = 3
2 + 3 = 4
...
"""
for i in range(len(counts) - 1):
    counts[i+1] += counts[i]
### counts = [1, 4, 5, 6, 8]

## DATA의 마지막 원소 1의 발생 횟수 counts[1]을 감소시키고 TEMP에 1을 삽입
"""
arr 인덱스 len(arr) - 1 => 0까지 돌면서
그 값이 counts의 인덱스
의 값 -1 이 temp의 인덱스
"""

temp = [0] * len(arr)
for i in range(len(arr)-1, -1, -1):
    counts[arr[i]] -= 1
    temp[counts[arr[i]]] = arr[i]
print(temp)