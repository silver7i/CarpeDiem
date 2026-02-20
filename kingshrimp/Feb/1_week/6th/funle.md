
# [2026-02-09] SWEA 1989. 초심자의 회문 검사

## 1. 문제 개요
- **목적**: 주어진 단어가 거꾸로 읽어도 같은 '회문(Palindrome)'인지 판별하기.
- **출력**: 회문이면 `1`, 아니면 `0`.



## 2. 해결 방법 (3가지 방식)

### 방법 1: Index 제어 (가장 권장하는 알고리즘적 사고)
문자열의 양 끝을 비교하며 중심부로 이동하는 방식입니다.

```py
word = input().strip()
N = len(word)
result = 1  # 기본값을 회문(1)으로 설정

for i in range(N // 2):
    # 왼쪽 끝(i)과 오른쪽 끝(N - 1 - i) 비교
    if word[i] != word[N - 1 - i]:
        result = 0
        break

```

> **Point**: 전체를 다 돌 필요 없이 절반(`N // 2`)만 확인하면 되므로 효율적입니다.

### 방법 2: Pythonic 슬라이싱

파이썬의 슬라이싱 기능을 활용해 코드를 극도로 단축합니다.

```py
word = input().strip()
result = 1 if word == word[::-1] else 0

```

> **Point**: 가독성이 좋고 구현이 매우 빠릅니다.

### 방법 3: Stack 자료구조 활용

LIFO(Last In First Out) 성질을 이용하여 문자를 역순으로 추출합니다.

```python
word = list(input().strip())
reversed_word = ""

while word:
    reversed_word += word.pop() # 뒤에서부터 하나씩 제거하며 추가

```

---

## 3. 핵심 Point (Self-Review)

1. **인덱스 계산**: 뒤에서 `i`번째 인덱스는 `N - 1 - i`임을 잊지 말자.
2. **효율성**: 회문 검사는 문자열 전체를 뒤집는 것보다, 중간까지만 검사하다가 틀린 지점에서 `break`하는 것이 더 빠르다.
3. **확장성**: 이 원리는 나중에 2차원 배열에서 가로/세로 회문을 찾는 문제(SWEA 1215번 등)의 기초가 된다.

---

#Algorithm #Python #SSAFY #Palindrome

```

