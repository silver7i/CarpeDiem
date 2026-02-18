# 딱지놀이


N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = A.pop(0)
    b = B.pop(0)
    A.sort(reverse=True)
    B.sort(reverse=True)
    flag = 0
    for i in range(a):
        for j in range(i, b):
            if A[i] == B[j]:
                break
            elif A[i] > B[j]:
                flag = 1
                break
            elif A[i] < B[j]:
                flag = 2
                break
        if flag != 0:
            break
    if flag == 0 and len(A) > len(B):
        print('A')
        continue
    if flag == 0 and len(A) < len(B):
        print('B')
        continue
    if flag == 1:
        print('A')
        continue
    if flag == 2:
        print('B')
        continue
    if flag == 0:
        print('D')
        continue

