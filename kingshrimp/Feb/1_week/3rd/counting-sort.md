TIL: 카운팅 정렬 (Counting Sort) 심화 - 음수 처리 및 안정 정렬
1. 음수 데이터 처리 원리 (Offset 활용)

카운팅 정렬은 값 자체를 리스트의 인덱스로 사용하므로 음수 인덱스 문제를 해결해야 함.

• 해결법: 데이터의 최솟값(`min_val`)을 찾아 모든 데이터에서 빼줌으로써 0 이상의 양수로 변환(Offset).

• 복구: 정렬된 결과를 만들 때 다시 `min_val`을 더해 원래 값으로 복원.

2. 안정 정렬 (Stable Sort) 구현 (누적합 활용)

단순히 개수만 세어 출력하면 입력 순서가 뒤섞임. 데이터의 상대적 순서를 유지하기 위해 다음 과정을 거침.

• 누적합 계산: 각 숫자가 결과 배열에서 가질 수 있는 '마지막 위치'를 계산.

• 역순 순회: 원본 배열을 뒤에서부터 읽으며 누적합 정보를 이용해 배치. 뒤에 있던 요소가 뒤에 배치되므로 안정성 유지.

3. Python 구현 코드

```py

def stable_counting_sort(array):

    if not array: return array

    

    max_val, min_val = max(array), min(array)

    range_size = max_val - min_val + 1

    count = [0] * range_size

    output = [0] * len(array)

    

    # 1. 빈도수 세기 (Offset 적용)

    for num in array:

        count[num - min_val] += 1

        

    # 2. 누적합 계산

    for i in range(1, range_size):

        count[i] += count[i - 1]

        

    # 3. 역순 순회로 안정성 확보

    for i in range(len(array) - 1, -1, -1):

        num = array[i]

        index = count[num - min_val] - 1

        output[index] = num

        count[num - min_val] -= 1

        

    return output

```

4. 핵심 요약

• 시간 복잡도: $O(n + k)$

• 공간 복잡도: $O(n + k)$

• 사용 시점: 데이터 범위(k)가 작고, 데이터 간 순서 유지가 중요할 때.
