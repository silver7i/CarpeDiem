# TIL (Today I Learned)

### 💡알고리즘 공부 Tip!
- 다른 사람이 작성한 코드 많이 읽어보기
- 코드를 눈이 아닌 손으로 따라하기
- 외워질 정도로 반복해서 풀어보기
---
### ⭕ 시간 복잡도
실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산
- __빅-오 표기법__(Big-O Notation)
  - 컴공에서의 log n 의 밑은 2  ⇒  log₂n
  - for 문이 쌓이면 O(n²), O(n³) … 늘어남

---
## List (= array)

#### 문제 푸는 방법
1. __입력 받은 정수를 1차원 배열에 저장하는 방법__
    - 정수 n을 입력 받고, 공백으로 구분된 정수들을 리스트로 입력 받는 코드
      ``` python
      N = int(input())
      arr = list(map(int, input().split()))
      ```
2. __배열 원소의 합 s 계산하기__
      ```python
      s = 0
      for i in range(N):
        s += arr[i]
      ```

3. __배열 원소 중 최댓값 max_v 찾기__

    ```python
    max_v = arr[0]   # 첫 원소를 최대로 가정
    for i in range(1, N)
      if max_v < arr[i]:
        max_v = arr[i]  # arr[i]가 더 크면 max_v 갱신
    ```

4. __배열 원소 중 최댓값의 인덱스 max_idx 찾기__

    ```python
    max_idx = 0
    for i in range(1, N):
      if arr[max_idx] < arr[i]:
        max_idx = i
    ```
    - 최댓값이 여러 개인 경우?
        - 가장 왼쪽의 최댓값 인덱스 값이 찾아짐
        - 같은 값일 때 마지막 인덱스를 찾고자 한다면??
            
            ↓↓↓↓       (같은 값일 때도 바꿔주면 됨.)
            

    4-1. __최댓값이 여러 개인 경우 마지막 인덱스 max_idx 찾기__

        ```python
        max_idx = 0
        for i in range(1, N):
          if arr[max_idx] <= arr[i]:
            max_idx = i
        ```

5. __찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1을 idx에 넣기__
    ```python
    # 입력 예시
    6 5
    2 7 5 3 1 7

    # 정수 N을 입력 받고, 공백으로 구분된 정수들을 리스트로 입력 받는 코드
    N, V = map(int, input().split()) # N, 찾는 값 V
    arr = list(map(int, input().split()))

    ################

    # 5를 찾는 경우
    idx = -1           # 찾는 값이 없다고 가정
    for i in range(N): 
      if arr[i] == V:  # arr[i]가 찾는 값이면
        idx = i        # 인덱스 저장
        break          # for i / break를 쓸 때는 어떤 루프를 탈출하는지 적어놓으면 좋음
    ```
