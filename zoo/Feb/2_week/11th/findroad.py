for _ in range(10):
# for _ in range(1):
    tc, e = map(int, input().split()) # tc 는 테스트 케이스, e는 간선수

    graph = list(map(int, input().split())) # 인접 리스트 만들기 도구

    adj_list = [[] for _ in range(101)] # 인접 리스트 틀 생성

    for k in range(len(graph)//2):
        i, j = graph[k * 2], graph[k * 2 + 1]
        adj_list[i].append(j) # 인접리스트 수정

    stack = []
    visited = [0] * 101
    start = 0

    while True:
        if start == 99:
            answer = 1
            break

        if visited[start] == 0:
            visited[start] = 1

        for y in adj_list[start]:
            if visited[y] == 0:
                visited[y] = 1
                stack.append(start)
                start = y
                break # for 탈출
        else:
            if stack:
                start = stack.pop()
            else:
                answer = 0
                break

    print(f"#{tc} {answer}")