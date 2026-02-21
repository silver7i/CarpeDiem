for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    count = 0
 
    for i in range(2, N-2):
        if max(building[i-2], building[i-1], building[i], building[i+1], building[i+2]) == building[i]:
            cnt = min(building[i] - building[i-1], building[i] - building[i-2], building[i] - building[i+1], building[i] - building[i+2])
            count += cnt
 
    print(f"#{tc} {count}")