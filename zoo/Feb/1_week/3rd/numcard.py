T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    a_i = input() # 문자열
    a_i = list(a_i)
    a_i = list(map(int, a_i)) # 리스트
 
    max_v = max(a_i)
    counts = [0] * (max_v + 1)
 
    for n in range(N):
        counts[a_i[n]] += 1 # counts 갱신 완
 
    for idx, val in enumerate(counts):
        max_val = 0
        for i in range(idx, -1, -1):
            if counts[i] > max_val:
                max_val = counts[i]
                idx = i
 
    print(f"#{tc} {idx} {max_val}")