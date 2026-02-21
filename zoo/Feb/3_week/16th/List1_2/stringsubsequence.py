T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    belt = input()
    target = input()
    
    current_idx = -1  # 현재 탐색 위치
    possible = True
    
    for char in target:
        # belt에서 char를 찾는데, current_idx + 1 위치부터 찾아라!
        found_idx = belt.find(char, current_idx + 1)
        
        if found_idx == -1:  # 못 찾으면 -1이 반환됨
            possible = False
            break
        
        current_idx = found_idx # 찾은 위치로 갱신
        
    if possible:
        print(f"#{tc} {current_idx}")
    else:
        print(f"#{tc} -1")