# TIL
1. IM 대비문제 풀기

---
## 오늘의 수업 : SW 문제 해결 기본 : Queue
---
## Queue (FIFO)
먼저 들어온 데이터가 먼저 나가는 선형 자료구조
```
q=list()
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)
print(q)
q.pop(0)  # pop()은 시간복잡도 O(1) 이지만
q.pop(0)  # 맨앞 또는 중간 값을 pop 할때에는 (예 pop(0))
q.pop(0)  # 시간복잡도가 O(n) 이지만
print(q)
```

---
## 선형 큐
데이터를 일렬로 저장하며, 앞에서 꺼내고 뒤에 넣는 기본 큐 구조\
문제점 : 삭제 여러번 하면 앞이 비는데 못씀
```
n = 3
que = [0]*n
front = rear -1

# enqueue()
rear += 1
que[rear] = 1  # enqueue(1)
rear += 1
que[rear] = 2  # enqueue(2)
rear += 1
que[rear] = 3  # enqueue(3)

while front != rear:  # front == rear 큐가 비어있는 상태
    front += 1
    tmp = que[front]
    print(tmp)
```

---
## 원형 큐
선형 큐의 공간 낭비를 막기 위해 처음과 끝이 연결된 구조
```
rear = (rear + 1) % size
front = (front + 1) % size
```

---
## 연결 큐
연결 리스트를 이용해 구현한 큐\
dee(덱) : 컨테이너 자료형 중 하나로 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너

```
from collections import deque # collections 모듈에 deque 클래스 사용
q=deque()
q.append(5)
q.append(6)
q.append(7)
q.append(8)
q.append(9)
print(q)
print([*q]) # *사용해서 deque 클래스 안의 값을 뺴온다음, 리스트로 감싸기
q.popleft()
q.popleft()
print([*q])
```

---
## 우선순위 큐
우선순위를 가진 항목들을 저장하는 큐

---
## 버퍼
데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역\
버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미
```
from collections import deque
p = 1  # 처음 줄 설 사람 번호
#q = []
q = deque()
N = 1000000  # 초기 마이쮸 개수
m = 0   # 나눠준 개수
v = 0

while m<N:
    #input()
    q.append((p, 1, 0))     # 처음 줄 서는 사람
    #print(q)
    v, c, my  = q.popleft()
    #print(f'큐에 있는 사람 수 {len(q)+1}, 받아갈 사탕 수{c}, 나눠준 사탕 수{m}')
    m += c
    q.append((v, c+1, my+c))    # 마이쮸를 받고 다시 서는 사람
    p += 1                  # 처음 줄서는 사람 번호
print(f'마지막 받은 사람 :{v}')
```

---
## BFS - 너비우선탐색
탐색 시작 정점에 인접한 정점들을 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
