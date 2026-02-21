t = int(input())

for tc in range(1, t+1):
    n = int(input()) # n: 카드 장수
    cards = list(map(int, input())) # n개의 숫자 ai가 여백없이 주어짐.

    # 출력 -> 가장 많은 카드의 숫자, 장 수
    count_box = [0] * 10 # 카드엔 0에서 9까지 숫자가 적힘

    for card in cards: # 카드 숫자를
        count_box[card] += 1 # 인덱스로 해서 몇장인지 카운트
    
    max_count = 0 # 가장 많은 카드의 장수
    max_idx = 0 # 가장 많은 카드의 숫자

    for i in range(10):
        if count_box[i] >= max_count:
            max_count = count_box[i]
            max_idx = i

    print(f"#{tc} {max_idx} {max_count}")