# t = int(input())

# for tc in range(1, t+1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))

#     ans_idx = M % N

#     print(f"#{tc} {arr[ans_idx]}")

"""
위 방법 말고 queue 로 풀어보자
"""

def q(N, M, arr):
    queue = []
    for i in range(N):
        queue.append(arr[i])
    
    front = 0

    for _ in range(M):
        front += 1
        ans = queue[front % N]
    
    return ans


t = int(input())

for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 출력: 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 맨앞 숫자 출력

    """
    필요한 거
    N: 큐 크기, M: 실행횧수, arr: 큐 내용물
    """
    print(f"#{tc} {q(N, M, arr)}")