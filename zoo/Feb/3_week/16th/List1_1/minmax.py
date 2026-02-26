t = int(input())

for tc in range(1, t+1):
    n = int(input())
    ai_list = list(map(int, input().split()))
    
    print(f"#{tc} {max(ai_list) - min(ai_list)}")