#  문제가 쉬운것 같으니 한번 클래스 써봐야지~~
#  전역변수를 공부를 하다가 멋있는 개발자는 전역변수를 쓰는것을 꺼려한다는것을 배웠다.
#  왜냐하면 전역변수를 선언을 하면 어디서 값이 바뀌는지 찾기가 어렵고 버그 유발자라고 한다.
#  그래서 멋있는 개발자들은 클래스를 사용을 하거나 return을 통해서 값을 따로 저장을 한다고 한다.
#  나도 멋있는 개발자의 발자취를 따라가고 싶어서 클래스로 해보았다.
#  클래스에 넣을 함수가 부족해서 정렬도 버블정렬 복습겸 다시 써본다.
#  아자아자

import sys

sys.stdin = open('swea-4466i.txt')

class Subject:
    def __init__(self, scores):
        self.array = scores

    def get_max_sum(self, k):
        # 정렬 후 k개 더하기
        return sum(sorted(self.array, reverse=True)[:k])


T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    N, K = map(int, sys.stdin.readline().split())
    scores_data = list(map(int, sys.stdin.readline().split()))

    # 클래스 출동!!!
    manager = Subject(scores_data)
    print(f"#{tc} {manager.get_max_sum(K)}")