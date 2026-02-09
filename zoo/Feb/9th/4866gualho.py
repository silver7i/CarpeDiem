t =int(input())

for tc in range(1, t+1):
    str = input()

    top = -1
    stack = [0] * 100
    ans = 1

    for s in str:
        if s in '{(':
            top += 1
            stack[top] = s
        elif s in '})':
            if top == -1:
                ans = 0
                break
            else:
                top -= 1
                if stack[top+1] == "{" and s == "}":
                    continue
                elif stack[top+1] == "(" and s == ")":
                    continue
                else:
                    ans = 0
                    break
    if top != -1:
        ans = 0
    print(f"#{tc} {ans}")


