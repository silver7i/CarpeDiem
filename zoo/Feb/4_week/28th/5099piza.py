def fire(size, cnt, cz):
    queue = []
    for i in range(size):
        queue.append((i+1, cz[i]))
    new_num = size
    last_num = 0
    while queue:
        curr_num, curr_time = queue.pop(0)

        last_num = curr_num
        curr_time //= 2

        if curr_time != 0:
            queue.append((curr_num, curr_time))
        else:
            if new_num < cnt:
                queue.append((new_num+1, cz[new_num]))
                new_num += 1
    return last_num



t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())

    cheeses = list(map(int, input().split()))

    """
    필요한것
    번호표, 남은 시간(처음엔 C 그 이후엔 C//2), 치즈 리스트
    """
    
    print(f"#{tc} {fire(N, M, cheeses)}")