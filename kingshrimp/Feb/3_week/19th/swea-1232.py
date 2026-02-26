def postorder(node):

    if tree[node][1].isdigit(): # (0종료 조건)1. 해당 노드의 값이 숫자이면 -> 그 숫자를 그대로 반환
        return int(tree[node][1])
    
    else: # 2. 숫자가 아니면 (자식 노드 존재) -> 후위 탐색 진행

        L = postorder(int(tree[node][2])) # (1) L : 왼쪽 노드로 이동

        R = postorder(int(tree[node][3])) # (2) R : 오른쪽 노드로 이동

        op = tree[node][1] # (3) V : 부모 노드를 조회

        if op == '+':
            return L + R
        
        elif op == '-':
            return L - R
        
        elif op == '*':
            return L * R

        else: return L / R

for tc in range(1, 11):

    V = int(input()) # 노드의 개수 V

    tree = [[] for _ in range(V+1)] # 인덱스와 노드번호를 맞추기 위함

    for _ in range(V): # 각 노드의 정보를 가져오는 반복문

        temp = input().split() # 각 트리의 0번째 인덱스에 접근하기 위해 노드 전체의 값을 temp에 임시 저장

        tree[int(temp[0])] = temp # 해당 인덱스에 노드 정보를 그대로 입력

    # print(tree) # 중간 점검 : 각 노드 정보가 노드 인덱스에 맞게 들어간 상태

    result = postorder(1) # 재귀 호출
    
    print(f"#{tc} {result:.0f}")