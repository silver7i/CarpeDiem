"""
1. 브레인 스토밍
일단 9명을 뽑아서 배열해야한다. 그런데 이미 1명을 뽑아놓은 상태이다.
-> 순서가 있는 배열이니 permutations를 
참고로 product는 중복 순열(주사위 2번던지기)
combination_with_replacement(사과, 배 중에서 3개 고르기)
4번타자에 1번 선수가 들어가야하니깐 순열을 만들고
슬라이싱을 한 이후에 4번자리에 넣어야한다.

한 이닝에 3명이 아웃을 당하면 이닝이 종료가 된다.
따라서 아웃카운트를 따로 기록을 해야한다.
-> for문에 아웃3이면 break를 걸지 아니면 while을 쓸지 고민

다음이닝에 다음 타선이 돌아야하니깐 타선도 기록해야한다.
-> 9명이 회전을 하니깐 %9를 통해서 관리를 해야한다.

점수를 기록을 해야하니깐 루상에 누가 있는지 알아야한다.
총점수도 기록을 해야한다.

최댓값 득점을 찾아야하니 max_val와 재할당 작업을 해야한다.
-> 재할당 작업은 값만 찾으면 되니깐 loop문이 아니라 max함수를
쓰는게 효율적이다.

순열 문제는 DFS로 풀어도 된다.

2. 판단 기준
1) DFS vs 순열
순열이 유리하다. 왜냐하면 가지치기(가지 자르기)가 불가능하기 때문이다.
시뮬레이션 중간에 어 이거 망했네?라고 탐색 종료를 할 수가 없기 때문이다.
그렇기 때문에 어차피 끝까지 가야하는 것이라면 순열로 돌리는것이 코드가 깔끔하다.

2) 비트마스크 vs 리스트
비트마스크가 유리하다.
루상의 주자를 확인을 할 때 리스트로 [1, 1, 1] 이런식으로 할 수도 있지만
메모리를 많이 먹는 이 문제에서 리스트를 줄여야한다.

3. 배운것
3-1. permutations은 print가 안됨
1) situation
- 백준 야구문제중 순열 생성
2) task
- array = permutations(range(1, 9), 8)
3) action
- 재미나이 물어봄
permutations는 바로 리스트를 보여주는게 아니라 제너레이터 객체를
변환을 하기 때문에 print해도 안나옴
- 해결방법
list로 감싸기
4) result
permutations는 list로 감싸자

3-2. tuple로 나왔을 때 리스트로의 변경
반복문을 돌리면서 순열로 뽑은 것들을 하나씩 list로 감싸면 됨.

3-3. 리스트에 중간 값 삽입 방법
.insert매서드를 사용하면 됨.
lineup.insert(3, 0)이런 방식
"""
import sys
from itertools import permutations

# sys.stdin = open('boj-17281-baseball.txt')

# 8명을 타자를 순열로 뽑자.
array = list(permutations(range(1, 9), 8))

# 1번선수를 4번타자 자리에 넣자
for players in array:
    lineup = list(p)
    lineup.insert(3, 0)
 