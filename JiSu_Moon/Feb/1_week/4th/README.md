# TLI
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
        if dy>4 or dy<0 or dx>4 or dx<0:  # 배열을 넘어갔을때
            continue
        Sum += arr[dy][dx]
        
result = Sum - arr[y][x]
print(result)
```

---

### 부분집합
