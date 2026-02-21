t = int(input())

for tc in range(1, t+1):
    graph = [input() for _ in range(5)]

    # 0 <= x <= 14
    # 0 <= y <= 4
    answer = ''

    max_len = 0
    for y in range(5):
        max_len = max(max_len, len(graph[y]))

    for x in range(max_len):
        for y in range(5):
            if 0 <= x < len(graph[y]):
                answer += graph[y][x]

    print(f"#{tc} {answer}")