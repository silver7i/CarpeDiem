import sys
# 대량의 입력을 빠르게 받기 위해 사용
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # 1. 테스트 케이스 정보 입력
    tc, length = input().split()
    
    # 2. 데이터 리스트 입력
    tc_list = list(input().split())

    # 3. 기준이 되는 숫자 리스트 (순서 중요!)
    num_system = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    # 4. 카운팅 딕셔너리 초기화
    # {'ZRO': 0, 'ONE': 0, ...}
    count_dict = {key: 0 for key in num_system}

    # 5. 개수 세기 (핵심 로직: O(N))
    for word in tc_list:
        count_dict[word] += 1

    # 6. 정렬된 결과 만들기 (재조립)
    result = []
    for num in num_system:
        # 해당 단어를 개수만큼 반복해서 리스트에 추가
        # extend는 리스트를 풀어서 넣어줌 ([1, 2] -> 1, 2)
        result.extend([num] * count_dict[num])

    # 7. 정답 출력
    print(tc)
    # 리스트 앞에 *를 붙이면 대괄호 없이 공백으로 구분되어 출력됨 (Unpacking)
    print(*result)