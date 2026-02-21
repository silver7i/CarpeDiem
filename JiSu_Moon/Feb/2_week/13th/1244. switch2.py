# 스위치 켜고 끄기


N = int(input())
arr = list(map(int, input().split()))
student = int(input())
S = [list(map(int, input().split())) for _ in range(student)]

for i in range(student):
    if S[i][0] == 1:  # 남학생
        idx = S[i][1]-1
        while idx < N:
            if arr[idx] == 1:
                arr[idx] = 0
            elif arr[idx] == 0:
                arr[idx] = 1
            idx += S[i][1]

    if S[i][0] == 2:  # 여학생
        idx = S[i][1]- 1
        if arr[idx] == 1:
            arr[idx] = 0
        elif arr[idx] == 0:
            arr[idx] = 1
        x = 1
        while 0<=idx-x and idx+x<N:
            if arr[idx-x] == arr[idx+x]:
                if arr[idx-x] == 1:
                    arr[idx-x], arr[idx+x] = 0,0
                elif arr[idx-x] == 0:
                    arr[idx-x], arr[idx+x] = 1,1
                x += 1
            else:
                break

# 출력형식 20개씩 끊어서 내야함 ;;
for i in range(N):
    print(arr[i], end=' ')
    if (i + 1) % 20 == 0:
        print()