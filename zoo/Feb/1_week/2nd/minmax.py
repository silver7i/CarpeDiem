T = int(input())
for tc in range(1, T+1): # range(T)
    N = int(input())
    arr = list(map(int, input().split()))

	  # max_v, min_v = 0, int(1e9) -> for도 수정해야
    max_v = arr[0]
    min_v = arr[0]

    # 최댓값 찾기
    for n in range(1, N):
        if max_v < arr[n]:
            max_v = arr[n]

    # print(max_v) -> 디버깅 습관
    
    # 최솟값 찾기
    for n in range(1, N):
        if min_v > arr[n]:
            min_v = arr[n]
            
    # print(min_v) -> 디버깅 습관

    print(f"#{tc} {max_v - min_v}")