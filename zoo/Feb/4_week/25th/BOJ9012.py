t = int(input())

for _ in range(t):
    paren_str = input()

    stack = []

    answer = "YES"

    for x in paren_str:
        if x == "(":
            stack.append(x)
        else:
            if not stack:
                answer = "NO"
                break # for x 탈출
            top = stack.pop()

    if stack:
        answer = "NO"

    print(answer)