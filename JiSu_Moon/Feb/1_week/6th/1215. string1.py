# [S/W 문제해결 기본] 3일차 - 회문1 


for tc in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    total = 0
 
    # 가로 회문 찾기
    for i in range(8):
        for j in range(8-N+1):
            for k in range(N//2):
                if arr[i][j+k] != arr[i][j+N-1-k]:
                    break
            else:
                total +=1
 
    # 세로 회문 찾기
    for i in range(8):
        for j in range(8-N+1):
            for k in range(N // 2):
                if arr[j + k][i] != arr[j+N-1-k][i]:
                    break
            else:
                total += 1
 
    print(f'#{tc} {total}')