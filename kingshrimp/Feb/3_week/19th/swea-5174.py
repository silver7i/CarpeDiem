T = int(input())
for test_num in range(1,1+T):


    graph = {}
    a,b = map(int,input().split())
    L = list(map(int,input().split()))
    # print(L)
    for i in range(0,2*a,2):
        if graph.get(L[i]):
            graph[L[i]] = graph[L[i]] + [L[i+1]]
        else:
            graph[L[i]] = [L[i+1]]
    S = []
    answer = 0
    S.append(b)
    while S:
        answer +=1
        visit = S.pop(0)
        if graph.get(visit):
            for i in graph[visit]:
                S.append(i)
        

    print(f'#{test_num} {answer}')