N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    queue = list(word)
    check = []
    now_char = ""
    is_char = True

    while queue:
        curr = queue.pop(0)

        if curr != now_char and curr in check:
            is_char = False
            break

        check.append(curr)
        now_char = curr

    if is_char:
        cnt += 1

print(cnt)
