# TIL
1. 알고리즘 보충수업
2. SWEA 1문제 풀기 
3. 라이브 수업 복습 

---
## 오늘의 수업 : SW 문제 해결 기본 : List 2-1
---
### 2차원 배열

```
arr = [list(map(int, input().split())) for _ in range(n)]
arr = [[0]*x for _ in range(y)]
```
```
# 지그재그 순회

for i in range(n):
    for j in range(m):
        f(arr[i][j + (m-1-2*j) * (i%2)])
```

---
### 델타

```
# 기준좌표에서 상하좌우 3칸씩 더하기

arr = [ [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8],
        [1, 2, 9, 1, 2],
        [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8]]

y,x=map(int,input().split())


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
Sum = 0

for d in range(4):
    for power in range(1,4):
        dy = y+di[d]*power
        dx = x+dj[d]*power
        if dy>4 or dy<0 or dx>4 or dx<0:  # 유효범위 검사
            continue
        Sum += arr[dy][dx]
        
result = Sum - arr[y][x]
print(result)
```

---
### 부분집합
주어진 집합에서 '뽑거나/안 뽑거나' 해서 만들 수 있는 모든 경우\
완전검색 + 선택/비선택 (비트 1/0)\
특정 조건 만족하는 조합 
```
arr = [3,6,7,1,5,4]

n = len(arr) 		# n : 원소의 개수

for i in range(1<<n) : 		# 1<<n : 부분 집합의 개수
    for j in range(n):		# 원소의 수만큼 비트를 비교함
        if i & (1<<j): 		# i의 j번 비트가 1인경우
            print(arr[j], end=", ")		# j번 원소 출력
    print()
print()
```