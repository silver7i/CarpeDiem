T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    P = [0] + list(map(int, input().split()))

    # visited라는 리스트를 만들어서 방문 했는지 안했는지를 기록을 한다
    visited = [0] * (N + 1)
    # 현재 방문 위치
    curr = 1
    # 움직임의 수 -> 최종 결과 
    moves = 0 
    
    #  명시적으로 언제까지 루프를 시킬것인지가 정해져있지 않기 때문에 for문이 아닌 while사용
    while curr < N:
        moves += 1
        if curr == 1:

            curr += 1
        else:

            if visited[curr] == 0:
                visited[curr] = 1 
                curr = P[curr]
            else:
                curr += 1
                
    print(f"#{tc} {moves}")