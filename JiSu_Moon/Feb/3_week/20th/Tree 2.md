# TIL
1. 밀린 강의 및 과제 풀기 (~stack까지)
2. 일타싸피 시험 준비

---
## 오늘의 수업 : SW 문제 해결 기본 : Tree 2
---
## 이진탐색 트리 (BST, Binary Search Tree)
- 데이터를 빠르게 검색할 수 있도록 체계적으로 저장
- 최대 O(log n)의 빠른 속도로 값을 검색할 수 있는 자료구조
- 빠르게 검색될 수 있도록, 특정 규칙을 갖는 이진 트리 형태로 값을 저장
- 왼쪽 < 부모 < 오른쪽 규칙을 가지는 트리

---
## 힙 (Heap)
완전 이진 트리에 있는 노드 중에서 키 값이 가장 크거나 작은 노드를 찾기 위해서 만든 자료구조 (완전이진트리 + 우선순위 규칙)
- 최대 힙(Max Heap)
    - 키 값이 가장 큰 노드를 찾기 위한 힙
    - 항상 {부모 노드의 키 값 > 자식 노드의 키 값} 조건을 만족
    - 루트 노드 : 키 값이 가장 큰 노드
- 최소 힙(Min Heap)
    - 키 값이 가장 작은 노드를 찾기 위한 힙
    - 항상 {부모 노드의 키 값 < 자식 노드의 키 값} 조건을 만족
    - 루트 노드 : 키 값이 가장 작은 노드
```
# 최대힙

def enq(n):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = n  # 마지막 정점에 key 추가

    c = last
    p = c // 2      # 완전이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]: # 부모가 있고, 부모 < 자식 인경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식
    while c <= last:        # 자식이 하나라도 있으면
        if c+1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1                      # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c               # 자식을 새로운 부모로
            c = p * 2           # 왼쪽 자식 번호를 계산
        else:                   # 부모가 더 크면
            break               # 비교 중단,
    return tmp

heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
while last:
    print(deq())
```
