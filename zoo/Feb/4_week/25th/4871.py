t = int(input())
 
for tc in range(1, t+1):
    # v 노드 수, e 간선 수
    v, e = map(int, input().split())
 
    # 인접리스트 생성
    adj_list = [[] for _ in range(v+1)]
 
    # 간선 출발노드 sn, 도착노드 en 인접리스트에 반영
    for _ in range(e):
        sn, en = map(int, input().split())
        adj_list[sn].append(en)
 
    # 출발 노드 s, 도착노드 g
    s, g = map(int, input().split())
    # 출력 -> s에서 g로 갈 수 있으면 1 출력. 없으면 0 출력.
     
    # 출발 노드 푸쉬
    stack = []
    # 방문했던 곳이면 체크
    visited = [0] * (v+1)
     
    answer = 0
 
    stack.append(s)
    visited[s] = 1
 
    while stack:
        top = stack.pop()
        for w in adj_list[top]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(top)
                stack.append(w)
                break
        else:
            if top == g:
                answer = 1
     
    print(f"#{tc} {answer}")