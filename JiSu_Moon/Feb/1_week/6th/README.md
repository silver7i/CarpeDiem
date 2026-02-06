# TLI
1. 알고리즘 보충수업
2. SWEA 1~2문제 풀기 
3. 라이브 수업 복습 

---
## 오늘의 수업 : SW 문제 해결 기본 : List 2-2
---
### 순차검색

---

### 이진검색
자료 가운데에 있는 항목의 키값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

```
n = int(input())  # 리스트의 길이
arr = list(map(int,input().split()))  # 리스트에 저장되는 값
target = int(input())


def binary_search(st, ed, target):
    while 1:
        mid = (st+ed)//2  # 미드인덱스 구하기(중간값)

        if arr[mid] == target:  # 찾으면 1 리턴
            return 1
        elif arr[mid] > target:  # 타켓이 미드 인덱스보다 작으면 왼쪽 탐색
            ed = mid-1
        elif arr[mid] < target:  # 타켓이 미드 인덱스보다 크면 오른쪽 탐색
            st = mid+1

        if st > ed:  # 못찾으면 0 리턴
            return 0


arr.sort()
ans = binary_search(0, n-1, target)  # 시작인덱스, end인덱스, 찾고자 하는값
if ans:
    print('찾았음')
else:
    print('없음')
```

---

### 선택정렬
1. 주어진 리스트에서 최솟값을 찾는다.
2. 리스트의 맨 앞에 위치한 값과 교환한다. 
3. 1번 2번 과정 반복
4. 미정렬 원소가 하나 남은 상황에서는 마지막 원소가 가장 큰 값을 갖게 되므로, 실행을 종료하고 선택정렬이 완료된다.

```
def selection_sort(a, N):
    for i in range(N-1):  # 정렬 구간의 시작 인덱스
        min_idx = i  # 첫 원소를 최솟값으로 가정 
        for j in range(i+1, N):
            if a[min_idx] > a[j]:  # 최솟값의 인덱스 갱신
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]  # 구간 최솟값을 구간 맨 앞으로
```

---

### 셀렉션 알고리즘

---

### 재귀함수

```
def abc(level):
    if level==5:
        print(level, end=' ')
        return

    print(level, end=' ')
    abc(level+1)
    print(level, end=' ')

abc(1)
print()
```

---

### parametric search

```
bettery="######____"   # 60%
# bettery="__________"   # 0%
# bettery="##########"   # 100%

def parametric_search(st,ed):
    Max=-1  # 아무것도 없으면 0% 를 출력해야하기 때문에
    while 1:
        mid=(st+ed)//2
        if bettery[mid]=='_':
            ed=mid-1
        elif bettery[mid]=='#':
            Max=mid
            st=mid+1
        if st>ed:
            break
    return Max+1

ans=parametric_search(0,9) # st, ed
print(f'배터리는 {ans*10}% 만큼 차 있습니다.')
```