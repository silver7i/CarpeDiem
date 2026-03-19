# TIL
1. BFS/DFS
2. 월말평가 준비

---
## 오늘의 수업 : Carpediem 화상 스터디
---
# 개념설명 / 개념의 여러 방식의 코드화 / 예시문제
인접행렬, 인접리스트

# DFS
깊이 우선 탐색
한 방향으로 끝까지 깊게 들어갔다가 더 이상 못 가면 되돌아오는 방식
경로 탐색, 백트래킹      


- 기본 코드 (스택/재귀)
```
def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
```

# BFS
너비 우선 탐색
탐색 시작 정점에 인접한 정점들을 모두 차례로 방문한 후에, 
방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식
최단거리 문제

- 기본 코드 (큐)
```
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
```

# 이진트리
모든 노드들이 2개 이내의 서브 트리를 갖는 특별한 형태의 트리
각 노드가 자식 노드를 최대한 2개까지만 가질 수 있음

포화 이진 트리 : 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
완전 이진 트리 : 1번부터 n번까지 빈자리가 없는 이진 트리 (왼쪽은 있지만 오른쪽이 없는..)


# 위상정렬
이건 모르겠는뎅..