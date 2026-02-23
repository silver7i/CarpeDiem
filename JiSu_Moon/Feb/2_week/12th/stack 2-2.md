# TIL
13~18 설 연휴 IM 대비 문제 풀기

---
## 오늘의 수업 : SW 문제 해결 기본 : Stack 2-2
---
## 부분집합
어떤 집합의 공집합과 자기자신을 포함한 모든 부분\
집합에서 일부 원소를 뽑는 것 (순서 상관 없음)
```
def backtrack(a, k, n):  # a 주어진 배열, k 결정할 원소, n 원소 개수
    c = [0] * MAXCANDIDATES

    if k == n:
        process_solution(a, k)  # 답이면 원하는 작업을 한다
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)


def construct_candidates(a, k, n, c):  # 후보 추천
    c[0] = True  # 원소의 포함 여부
    c[1] = False
    return 2


def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end='')
    print()


MAXCANDIDATES = 2
NMAX = 3
a = [0] * NMAX
num = [1, 2, 3]
backtrack(a, 0, 3)
```

---
## 순열1
원소를 순서 있게 나열
```
def backtrack(a, k, n):
    c = [0] * MAXCANDIDATES

    if k == n:
        for i in range(0, k):
            print(a[i], end="")
        print()
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k + 1, n)

def construct_candidates(a, k, n, c):
    in_perm = [False] * (NMAX + 1)

    for i in range(k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(1, NMAX + 1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates

MAXCANDIDATES = 3
NMAX = 3
a = [0]*NMAX
backtrack(a, 0, 3)
```

---
## 가지치기 (Pruning)
```
def f(i, k, s, t):  # i원소, k 집합의 크기, s i-1까지 고려된 합, t목표
    global cnt
    global fcnt
    fcnt += 1
    if s > t:   # 고려한 원소의 합이 찾는 합보다 큰경우
        return
    elif s == t:    # 남은 원소를 고려할 필요가 없는 경우
        cnt += 1
        return
    elif i == k:    # 모든원소 고려
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함

#A = [1,2,3,4,5,6,7,8,9,10]
N = 10
A = [ i for i in range(1, N+1)]

key = 55
cnt = 0
bit = [0]*N
fcnt = 0
f(0,N,0,key)
print(cnt, fcnt)      # 합이 key인 부분집합의 수
```

---
## 순열2
"어차피 정답 안 되는 경우는 더 안 본다"
```
def f(i, N):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    if i == N:  #
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)   # i+1자리 결정
            p[i], p[j] = p[j], p[i]

p = [0,1,2]
N = 3
f(0, N)
```

---
## 분할정복
문제를 쪼개고 → 해결하고 → 합친다\
분할 : 해결할 문제를 여러 개의 작은 부분으로 나눈다.\
정복 : 나눈 작은 문제를 각각 해결한다.\
통합 : (필요하다면) 해결된 해답을 모은다.