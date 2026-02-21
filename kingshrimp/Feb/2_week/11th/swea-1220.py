# ===
# 1. 브레인 스토밍
# 테이블 위에 있는 자석들의 순서가 중요하다.
# 혼자 있는거 무조건 아웃
# 두개가 있는경우 서로 다른극이 있어야하고 s극이 위, n극이 아래
# *무조건 맨윗라인은 n극이어야하고 맨 아래 라인은 s극이어야한다.
# 위아래 메트릭스 정리하기
# 그러면 교착상태는 몇개로 봐야하는가?
# 교착은 n극과 s극이 만나는 경우만 교착이고 한개의 자석이 두개의 교착을 가져갈수는 없다.
# 맨위가 n이므로 그 다음에 색이 바뀔때마다 체크를 한다.
# 어차피 1, 3, 5이런식으로만 색이 바뀐다.
# 교착개수 구할때에는 색변환 값 +1에 나누기 2를 한다.
#
# 2. 구현 방식
# 1) 메트릭스 위는 n극, 아래는 s극으로 정리하기
#   - zip을 사용을 해서 행, 열 바꾸기
#   - n극 자석이 왼쪽, s극 자석이 오른쪽에 존재
#   - 새 메트릭스 생성
#   - 1행부터 왼쪽끝 s극이 먼저 발겨되면 아웃, n극이 발견되면 ok
#   - 100행부터 줄여가면서 n극이 먼저발견되면 아웃, n극이 발견되면 ok
# 2) 1
# - 그 사이에 색변환 개수 세기
#   - 1행 첫열부터 찾는데 현재상태 플래그 적기 파란색 발견 카운트 증가,
#     플래그가 이번에 파란색일때 if문을 만들어서 빨간색발견하면 카운트 증가
# 3) 출력값 정리: 카운트 +1을 한 이후 2로 나누기
# 4) 코드 쓰기 레츠꼬우
#
# 3. 배운점
# 1) zip을 사용할때 *을 붙여야하고 list로 감싸도 안에는 튜플로 나온다.
# 결국 list comprehension을 써야한다.
# 2) 글로벌 변수 선언은 read만 하는경우는 필요없다.
# write, update를 할 때에만 필요하다.
# 3) 함수의 return은 바로 print를 할 수 없다. 어디든 받아줘야한다.
# ===

import sys

sys.stdin = open('swea-1220i.txt')

red = 1
blue = 2
blank = 0
def make_matrix(N, matrix):
    #  가독성을 위해 숫자들을 색으로 명칭
    # TODO: 아 zip함수 오랜만에 써서 헷갈렸다.
    #  *붙이고 리스트함수로 또 감싸기
    # new_matrix = list(zip(*matrix))
    # 튜플아 여기는 너가 있어야할 장소가 아니다
    new_matrix = [list(row) for row in zip(*matrix)]

    # 1. 메트릭스 양쪽 n,s 떨궈버리기
    for r in range(N):
        for c in range(N):
            if new_matrix[r][c] == red:
                break
            elif new_matrix[r][c] == blue:
                new_matrix[r][c] = blank
        for c in range(N-1, -1, -1):
            if new_matrix[r][c] == blue:
                break
            elif new_matrix[r][c] == red:
                new_matrix[r][c] = blank
    return new_matrix

#  2. 뭔가 함수를 2개를 써서 풀면 멋있을것 같아!!
def find_color(matrix):
    cnt = 0
    for r in range(N):
        curr_color = red
        for c in range(N):
           if matrix[r][c] == red and curr_color == red:
               curr_color = blue
           elif matrix[r][c] == blue and curr_color == blue:
               cnt += 1
               curr_color = red
    return cnt


T = 10

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    fined_matrix = make_matrix(N, matrix)
    res = find_color(fined_matrix)
    print(f'#{tc} {res}')




