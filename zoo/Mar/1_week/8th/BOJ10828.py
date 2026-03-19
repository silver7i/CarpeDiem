import sys

N = int(sys.stdin.readline())

stack = [0] * N
top = -1
for _ in range(N):
    com = sys.stdin.readline().split()

    if com[0] == "push":
        top += 1
        stack[top] = com[1]

    if com[0] == "pop":
        if top == -1:
            print(top)
        else:
            top -= 1
            print(stack[top + 1])

    if com[0] == "size":
        print(top + 1)

    if com[0] == "empty":
        if top == -1:
            print(1)
        else:
            print(0)

    if com[0] == "top":
        if top == -1:
            print(top)
        else:
            print(stack[top])
