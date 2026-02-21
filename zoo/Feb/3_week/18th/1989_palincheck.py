t = int(input())

for tc in range(1, t+1):
    word = input()

    answer = 0
    if word == word[::-1]:
        answer = 1

    print(f"#{tc} {answer}")