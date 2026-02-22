def inorder(t):
    global ans
    if t:
        inorder(left[t])
        ans.append(t)
        inorder(right[t])

T = 10

for _ in range(1, T+1):
    V = int(input())  # 노드의 수

    left = [0] * (V+1)
    right = [0] * (V+1)
    letter = [0] * (V+1)  # 각 노드의 번호에 할당된 글자를 저장할 리스트
		
		# 완전 이진 트리이므로 이렇게 해도 돌아감..
    for i in range(1,V+1):
        if i*2 <= V:
            left[i] = i*2
        if i*2+1 <= V:
            right[i] = i*2+1
        letter[i] = list(input().split())[1]
		
		# 노드 번호로 중위순회 후 글자로 변환
    ans = []
    inorder(1)
    word = ''
    for i in ans:
        word += letter[i]
    
    print(f"#{_} {word}")