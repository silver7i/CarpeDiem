# 빙고


bingo = [list(map(int, input().split())) for _ in range(5)]
call = [list(map(int, input().split())) for _ in range(5)]

def find(n):  # 사회자가 부른 숫자 찾는 함수
    for y in range(5):
        for x in range(5):
            if bingo[y][x] == n:
                bingo[y][x] = 1  # 찾은 위치를 1로 표시

def line():  # 빙고 라인 검사 함수
    line = 0
    for i in range(5):
        # 가로
        if bingo[i][0] == 1:
            for d in range(5):
                if bingo[i][d] != 1:
                    break
            else:
                line += 1
        # 세로
        if bingo[0][i] == 1:
            for d in range(5):
                if bingo[d][i] != 1:
                    break
            else:
                line += 1
    # \
    if bingo[0][0] == 1:
        for d in range(5):
            if bingo[d][d] != 1:
                break
        else:
            line += 1
    # /
    if bingo[0][4] == 1:
        for d in range(5):
            if bingo[d][4-d] != 1:
                break
        else:
            line += 1

    return line

count = 0
flag = 0
for i in range(5):
    for j in range(5):
        find(call[i][j])  # 사회자가 부른 숫자 위치 찾기
        count += 1
        if count > 11:
            check = line()
            if check >= 3:
                flag = 1
                break
    if flag:
        break

print(count)
