# TIL
1. 알고리즘 보충수업
2. SWEA 2문제 풀기 (3문제 성공)
3. 라이브 수업 복습 

---
## 오늘의 수업 : SW 문제 해결 기본 : string
---
### 코드체계
컴퓨터가 처리할 수 있도록 문자에 고유한 숫자를 부여하는 것
아스키 문자 : 문자 인코딩 표준\
유니코드 : 다국어 처리를 위한 표준 코드체계\
유니코드 인코딩 : UTF-8(in web), UTF-16(in windows, java), UTF-32(in unix)\
전 세계의 모든 문자를 컴퓨터가 일관되게 표현하고 처리하는 것이 코드체계의 핵심

---
### 문자열
문자들이 순서대로 나열된 데이터

---
### 연산
1. 문자열 뒤집기 : [::-1], list.reverse()
2. 회문
```
'''
길이가 4인 회문을 찾는 예
4
CBBCABBA
'''

N = int(input())
txt = input()
total = 0
for j in range(8-N+1):      # 회문을 확인하는 구간의 첫 글자 인덱스
    for k in range(N//2):   # 회문의 길이 절반만큼 비교
        if txt[j+k] != txt[j+N-1-k]:
            break   # 비교 글자가 다르면 현재구간 중지
    else:       # break에 걸리지 않고 for 종료, 회문이면
        total += 1
print(total)
```
3. 문자열 비교 : == 연산자와 is 연산자
4. 사전 순서 비교 : 비교연산자 < 사용
5. 문자열 숫자를 숫자로 변환 : int(), float(), str()

---
### 고지식한 패턴 검색
```
def pattern_count(p, t):    # 패턴의 등장 횟수 리턴
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
        if j==M:     # 패턴을 찾은 경우
            cnt += 1
            i = i - j + 1
            j = 0
    return cnt
```
```
t = 'TTTTTATTAATA'
p = 'TZA'

def search(p, t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):  # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(M):      # p에서 비교할 위치 인덱스
            if t[i+j]!=p[j]:
                break
        else:               # break에 걸리지 않고 for가 끝난경우 실행
            return i        # 패턴이 처음 나타난 인덱스 리턴
    return -1               # t에 p패턴이 없는 경우

print(search(p, t))
```

---
### KMP 알고리즘
```
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)
    # preprocessing
    j = 0 # 일치한 개수== 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j          # p[i]이전에 일치한 개수
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    # search
    i = 0   # 비교할 텍스트 위치
    j = 0   # 비교할 패턴 위치
    while i < N and j <= M:
        if j==-1 or t[i]== p[j]:     # 첫글자가 불일치했거나, 일치하면
            i += 1
            j += 1
        else:               # 불일치
            j = lps[j]
        if j==M:    # 패턴을 찾을 경우
            print(i-M, end = ' ')    # 패턴의 인덱스 출력
            j = lps[j]

    print()
    return
```

---
### 보이어-무어 알고리즘

---
### 문자열 암호화

---
## 실습
1. 매개변수 Sum을 사용해서 누적합 출력하기
출력결과: 3 7 12 13 14 28
```
arr = [3, 4, 5, 1, 6, 9]

def abc(level, Sum):  # 매개변수(지역변수)
    print(Sum, end=' ')
    if level == 5:
        return
    abc(level+1, Sum+arr[level+1])

abc(0, arr[0])
```

2. Sum 이라는 전역변수를 이용해서 누적합 출력하기
```
arr = [3, 4, 5, 1, 6, 9]
Sum = arr[0]  # 전역변수

def abc(level):
    global Sum
    print(Sum, end=' ')
    if level == 5:
        return
    Sum += arr[level+1]
    abc(level+1)

abc(0)
```

3. 3개의 카드 묶음이 잇는데, 각 묶음에서 카드 1장씩 뽑았을때 나올수 있는 합을 모두 출력하기

```
# 매개변수
arr = [3, 7, 1, 2]

def abc(level, Sum):
    if level == 3:
        print(Sum, end=' ')
        return

    for i in range(4):
        abc(level+1, Sum+arr[i])

abc(0,0)  # level Sums
print()


# 전역변수
arr = [3, 7, 1, 2]
Sum = arr[0]

def abc(level):
    global Sum
    if level == 3:
        print(Sum, end=' ')
        return

    for i in range(4):
        Sum += arr[i]
        abc(level+1)
        Sum -= arr[i]


abc(0)  # level Sums
```