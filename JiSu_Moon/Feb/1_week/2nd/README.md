# TLI
1. 라이브 수업 복습
2. SWEA 1문제 풀기 (시간이 된다면 나머지도..)
3. 알고리즘 보충수업 사전테스트 응시

---
## 오늘의 수업 : SW 문제 해결 기본 : List 1-1
---
### 알고리즘(Algorithm) : 문제를 해결하기 위한 절차나 방법
#### 알고리즘의 성능
- 정확성 : 얼마나 정확하게 동작하는가
- 작업량 : 얼마나 적은 연산으로 원하는 결과를 얻어내는가
- 메모리 사용량 : 얼마나 적은 메모리를 사용하는가
- 단순성 : 얼마나 단순한가
- 최적성 : 더이상 개선할 여지 없이 최적화 되있는가

---

### 시간 복잡도
time complexity (누구의 코드가 더 빠르게 문제 해결)
시간복잡도 = 기본 연산 수행 횟수 + 입력되는 데이터를 종합적으로 고려
- 빅-오(Big-O Notation)
시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
계수는 생략하여 표시

---

### 정렬
2개 이상의 자료를 키(특정 기준)에 의해 작은 값부터 큰 값 혹은 그 반대의 순서대로 재배열
1. 버블 정렬
arr = [6, 3, 87, 3, 23, 4]
for e in range(len(arr)-1, 0, -1):  # 앞이던 뒤던 똑같음
    for c in range(e):
        if arr[c+1] < arr[c]:
            arr[c+1], arr[c] = arr[c], arr[c+1]
print(arr)

2. 선택 정렬
arr = [6, 3, 87, 3, 23, 4]
for i in range(len(arr)):
    for j in range(i+1, len(arr), 1):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

3. 삽입 정렬 (빈리스트 생성)
arr = [6, 3, 87, 3, 23, 4]
ret = []
for i in range(6):
    ret.append(arr[i])
    for j in range(i, 0, -1):
        if ret[j] < ret[j-1]:
            ret[j], ret[j-1] = ret[j-1], ret[j]
print(ret)

---

### 디버깅
어디서부터 잘못되었는지 찾는 행위( 뭐가 잘못되었다고 안알려줌)
#### 디버깅 단축키
- Ctrl + F8 : Toggle breakpoint
- shift + F9 : 디버깅 시작
- F8 : Step over
- F7 : Step into
- F9 : resume (다음 breakpoint 까지 실행)
- Ctrl + F2 : 디버깅 종료