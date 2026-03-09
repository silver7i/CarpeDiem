# TIL
1. 라이브수업 복습
2. SWEA 과제 (1문제)

---
## 오늘의 수업 : 완전검색/그리디 1
---
### 반복과 재귀
함수 호출할 때, int 타입 객체를 전달하면 값만 복사됨\
함수가 끝나면, 해당 함수를 호출했던 곳으로 돌아옴\
무한 재귀호출을 막기 위하여 if문을 사용한 기저조건(base case) 필수\
```
# 상태 공간 트리의
# - 높이 : 기저조건 (종료조건)
# - 가지의 수 : 재귀호출 수
#   - 가지의 수가 많다면 반복문으로 만들 수 있다
# - 핵심
#   - 1. 상태공간 트리 그리기
#   - 2. 트리를 보고 코드로 구현하기
def recur3(num):
    # 트리의 높이와 같다
    if num > 3:
        return

    # 가지의 수 만큼 재귀호출 코드가 돌아간다.
    for i in range(1, 7):
        recur3(num + 1)
```

---
### 순열
서로 다른 N개에서, R개를 중복없이, 순서를 고려하여 나열하는 것\

1. 먼저 path 라는 전역 리스트 준비
2. level = if 문(기저조건) , branch = for 문 (반복) ⇒ 재귀 코드 구현
3. 재귀호출을 하기 직전에 이동할 곳의 위치를 path 리스트에 기록 (append)
4. 바닥에 도착했으니 출력하는 코드 수행 (print)

### 중복순열
구현 원리
1. 재귀호출을 할 때마다, 이동 경로를 흔적으로 남김
2. 가장 마지막 레벨에 도착했을 때, 이동 경로를 출력

```
path = []


def recur(cnt):
    if cnt == 2:
        print(path)
        return

    # 한 번의 선택에서 3가지 경우의 수
    for i in range(3):
        # [주의!!!!!!!!] in 은 O(N) 이라서 너무 느리다! 시간초과 가능성이 너무 높다.
        if i in path:  # 이미 뽑은 숫자라면 다음 숫자를 고려하자
            continue

        path.append(i)
        recur(cnt + 1)
        path.pop()

recur(0)

# --------------------- 중복없애기

path = []
N = 7
used = [0] * N  # N 개의 종류가 있을 경우 N개 만큼 만든다.

def recur2(cnt):
    if cnt == 3:
        print(*path)
        return

    for i in range(1, 7):
        if used[i]:     # 이미 i 를 사용한 적이 있다면
            continue

        used[i] = 1     # 방문처리
        path.append(i)
        recur2(cnt + 1)
        path.pop()
        used[i] = 0     # 방문기록 초기화


recur2(0)
```

---
### 완전탐색
모든 가능한 경우를  시도해서 정답을 찾아내는 알고리즘

1. 주사위 눈의 합
2. 연속 3장의 트럼프 카드
3. Baby-gin