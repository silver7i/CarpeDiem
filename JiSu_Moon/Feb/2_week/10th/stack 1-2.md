# TIL
1. SWEA 4문제 풀기

---
## 오늘의 수업 : SW 문제 해결 기본 : Stack 1-2
---
## 재귀호출
함수가 자신과 같은 작업을 반복해야 할 때, 자신을 다시 호출하는 구조
ex) factorial, 피보나치 수열

```
# 재귀함수의 기본형

def f(i, N):
    if i==N:    # 중단조건
        return
    else:  # 재귀호출
        f(i+1, N)

f(0, 3)
```
```
# 모든 배열 원소에 접근하는 재귀함수

def f(i, N): # i 배열 인덱스, N 배열크기
    if i==N:    # 중단조건
        return
    else:  # 재귀호출
        print(A[i])
        f(i+1, N)

A = [1,2,3]
f(0, 3)
```
```
# 배열 원소 V 검색 

def f(i, N, V): # i 배열 인덱스, N 배열크기, V 찾는 값
    if i==N:    # V가 없는 경우  (배열을 벗어남)
        return 0
    elif A[i] == V: # 찾은 경우
        return 1
    else:  # 재귀호출
        return f(i+1, N, V)

N = 3
A = [3, 7, 6]
#V = 2
V = 6
ans = f(0, N, V)
print(ans)
# print(f(0, N, V))
```

---
## Memoization - 재귀 알고리즘 최적화
컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술 (중복 계산 제거 기술)
DP를 구현하는 방법 중 하나
```
def fibo1(n) :
    global cnt
    cnt += 1
    if n >= 2 and memo[n] == 0 :
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

n = 10
cnt = 0                 # 호출 횟수 기록
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo1(n), cnt)

✔ n → 지역변수 (스택마다 따로 존재)
✔ memo → 전역변수 (모든 호출이 공유)
✔ cnt → 전역변수 (재할당하므로 global 선언 필요)
```

---
## DP - 최적화를 위한 알고리즘
입력 크기가 작은 부분 문제들을 먼저 해결한 뒤, 그 결과를 바탕으로 더 큰 부분 문제를 차례대로 해결해 나가며 최종적으로 전체 문제의 해답을 도출하는 알고리즘
```
def fibo2(n) :
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1) :
        f[i] = f[i-1] + f[i-2]

    return f[n]

print(fibo2(10))
```

---
## DFS (깊이 우선 탐색)
한 방향으로 가능한 한 깊게 탐색한 후, 더 이상 갈 곳이 없으면 되돌아와 다른 방향을 탐색
가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출(LIFO) 구조의 스택 사용
```
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(start, N): # 모든 정점을 중복없이 빠짐없이 방문
    visited = [0] * (N + 1)     # 방문기록 배열 생성
    stack = []                  # 스택 생성
    v = start                   # 시작점 방문 (방문한 위치 v)
    print(v)                    # 방문해서 할 일 - 정점 번호 출력
    visited[v] = 1              # 방문 표시

    while True:                 # 반복
        for w in adj_list[v]:   # 현재 방문한 v에 인접한 정점 w가 있고
            if visited[w] == 0: # 아직 방문 전이면
                stack.append(v)     # 막혔을 때 되돌아올 자리 push
                visited[w] = 1      # 방문 표시
                v = w  # w를 현재 방문한 위치로
                print(v)
                # w를 새로운 방문지 v로 해서 반복 -> for w로 이동
                break       # for w, 새로 이동한 정점 v부터 다시 탐색 반복
        else:                   # v에 인접한 w가 더이상 없으면
            if stack:           # 최근에 지나온 곳부터 다시 탐색
                v = stack.pop()
            else:               # 남은 경로가 없으면/스택이 비어있으면
                break           # while True



V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]         # 인접 리스트
for i in range(E):
    v, w = graph[i*2], graph[i*2+1]     #

    adj_list[v].append(w)
    adj_list[w].append(v)                 # 방향이 없는 경우

dfs(1, V)                           # 1번부터 탐색
```