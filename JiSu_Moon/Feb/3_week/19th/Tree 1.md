# TIL

---
## 오늘의 수업 : SW 문제 해결 기본 : Tree 1
---
## Tree 
비선형 자료구조
### 용어 정리
노드 : 트리의 원소\
간선 : 노드를 연결하는 선. 부모 노드와 자식 노드를 연결\
루트 노드 : 트리의 시작 노드\
형제 노드 : 같은 부모 노드의 자식 노드들\
조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들\
서브 트리 : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리\
자손 노드 : 서브 트리에 있는 하위 레벨의 노드들\
노드의 차수 : 연결된 자식 노드의 수\
트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값\
단말 노드 : 차수가 0인 노드, 자식 노드가 없는 노드\
노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨\
트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨\

---
## 이진트리
모든 노드들이 2개 이내의 서브 트리를 갖는 특별한 형태의 트리\
각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있음\
높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개\

- 포화 이진 트리 : 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 완전 이진 트리 : 높이가 h이고 노드 수가 n개일 때
- 편향 이진 트리 : 높이가 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진트리

```
def postorder(T):
    if T == 0:
        return 0
    l = postorder(left[T])
    r = postorder(right[T])
    return l + r + 1

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E + 1   # 정점 개수 = 간선 수 + 1

    left = [0] * (V + 1)
    right = [0] * (V + 1)
    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    cnt = postorder(N)
    print(f'#{tc}{cnt}')
```
---
## 순회
트리의 각 노드를 중복되지 않게 전부 체계적으로 방문하는 것

1. 전위 순회 : 부모 - 좌 자식 - 우 자식
2. 중위 순회 : 좌 자식 - 부모 - 우 자식
3. 후위 순회 : 좌 자식 - 우 자식 - 부모
```
arr=" ABCDEFG"

def _order(now):

    if now > len(arr)-1: 
	      return
    print(arr[now],end=' ')  # 전위 순회
    post_order(now*2)
    print(arr[now],end=' ')  # 중위 순회
    post_order(now*2+1)
    print(arr[now],end=' ')  # 후위 순회

post_order(1)
```