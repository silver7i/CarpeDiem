# 창고 다각형


N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
num.sort()

# 최대 높이 기둥의 x 찾기
best_idx = num[0][0]
Max = -1
for x, h in num:
    if h > Max:
        Max = h
        best_idx = x

st_idx = num[0][0]
ed_idx = num[-1][0]

# x좌표를 인덱스로 쓰는 높이 배열 만들기
arr = [0] * (ed_idx + 1)
for x, h in num:
    arr[x] = h

Sum = 0
# 면적 더하기 (왼 -> best_x)
nowh = 0
for i in range(st_idx, best_idx+1):
    if nowh < arr[i]:
        nowh = arr[i]
    Sum += nowh
# 면적 더하기 (오 -> best_x) (역방향)
nowh = 0
for i in range(ed_idx, best_idx, -1):
    if nowh < arr[i]:
        nowh = arr[i]
    Sum += nowh

print(Sum)