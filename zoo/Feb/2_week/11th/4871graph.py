t = int(input())

# V개 이내의 노드, E개의 간선
# 경로가 있으면1, 없으면 0

for tc in range(1, t+1):
    V, E = map(int, input().split()) # V 노드수, E 간선수

    adj_list = [[] for _ in range(V+1)] # 인접 리스트
    stack = [] # 스택 리스트
    visited = [0] * (V+1)

    for _ in range(E):
        i, j = map(int, input().split())
        adj_list[i].append(j) # 인접 리스트 담기

    S, G = map(int, input().split()) # S 출발, G 도착착

    while True: # 반복
        if S == G:
            answer = 1
            break

        if visited[S] == 0:
            visited[S] = 1


        for v in adj_list[S]: # 노드 인접리스트 확인해서

            if visited[v] == 0: # 방문한 적이 없으면
                stack.append(S) # 노드 스택에 남기고

                S = v # v로 이동

                break # for 탈출
        else:
            if stack:
                S = stack.pop()

            else:
                answer = 0
                break

    print(f"#{tc} {answer}")