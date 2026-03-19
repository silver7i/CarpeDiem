# TIL
1. 라이브수업 복습
2. SWEA 과제 (1문제)

---
## 오늘의 수업 : 분할정복
---
## 분할 정복
문제를 작은 하위 문제로 나누고(분할) 각각을 해결(정복)한 뒤,
그 결과를 결합(통합)하여 원래 문제를 해결하는 알고리즘 기법\

1. Divide (분할) → 문제를 작은 문제로 나눔
2. Conquer (정복) → 작은 문제를 해결
3. Combine (결합) → 결과를 합쳐서 원래 문제 해결

### 병합 정렬 (정렬)
여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식\
- 시간복잡도 : O(N log N)
- 정렬하면서 새로운 배열에 임시 저장하며 병합 (제자리 정렬 X)
- 추가 메모리 사용
- 함수가 자기자신을 호출하는 재귀 구조로 구현

### 퀵 정렬
기준값을 중심으로 주어진 배열을 두 개로 분할하고, 각각을 정렬하여 전체 배열을 정렬하는 방식\
별도의 병합 과정 불필요\
시간복잡도 : O(N log N)\
#### Partitioning
Pivot을 기준으로 왼쪽에는 Pivot 보다 작은 수, 오른쪽에는 큰 수 배치(정렬 안됨)\
구현 방법
1. Hoare Partition : 양쪽에서 포인터 이동, 잘못된 값 발견하면 swap
2. Lomuto Partition : 한쪽에서 진행, 구현 쉬움, swap 많음
```
# 퀵 정렬 중 lomuto partition 을 활용한 코드입니다.
# i, j 가 hoare 와는 다르게 앞에서부터 함께 이동한다는 점을 이해해주시면 됩니다.
#  - hoare 와 동일하게 i 는 pivot 보다 큰 값을, j 는 작은 값을 찾아나갑니다.

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]


def lomuto_partition(left, right):
    pivot = arr[right]

    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(left, right):
    if left < right:
        pivot = lomuto_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


quick_sort(0, len(arr) - 1)
print(arr)
```

### 이진 검색 (값 찾기)
자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법\
** 정렬된 배열 필요\
시간복잡도 : O(log N)