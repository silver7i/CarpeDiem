t = int(input())

for tc in range(1, t+1):

    txt = input()

    stack = []

    sum = 0

    for i in range(len(txt)):
        if txt[i] == '(':
            stack.append(txt[i])
        else:
            top = stack.pop()
            if txt[i-1] == '(':
                sum += len(stack)
            else:
                sum += 1

    print(f"#{tc} {sum}")