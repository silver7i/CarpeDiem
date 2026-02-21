"""
아이디어
2차원 리스트인데 컬럼과 로우의 관계가 전혀 없다. 
로우만 먼저 계산 하나씩하고 컬럼으로 돌아가도 되겠다.
if문을 써서 높이차이가 1인지 먼저 확인을 한다. 
이미 그 위치에 있는지를 판단을 해야한다.
길이가 L이 맞는지를 판단을 해야한다.

경사로를 넣었는지 안넣었는지 판단을 하기 위해서
list를 만들어서 관리하는 방법, 숫자를 변경을 하는 방법

for vs while
이거는 규칙적인 반복문이므로 for을 쓰는게 맞다

길이 L인지 판단
L이 아니라면 continue를 사용을 해서 넘기면 된다.

변수 설정
경사로
경사로 확인 리스트

열 탐색
zip함수를 사용해서 뒤집은 이후에 탐색

"""

import sys

def solve():
    T = int(input())
    for tc in range(1, T + 1):
        N, L = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(N)]
        
        # 메트릭스 생성
        # zip을 사용해서 컬럼 찾기 딸깍
        total_lines = board + [list(row) for row in zip(*board)]
        
        answer = 0
        
        for line in total_lines:
            if check_path(line, N, L):
                answer += 1
                
        print(f"#{tc} {answer}")

def check_path(line, N, L):
    # 아이디어: 경사로 설치 여부를 판단하기 위한 리스트, 이거 아니면 방문한 곳 -1로 처리방법도 있음
    visited = [False] * N
    
    # 규칙적인 반복문 for 사용
    for i in range(N - 1):
        # 1. 높이가 같으면 그대로 진행
        if line[i] == line[i+1]:
            continue
        
        # 2. 높이 차이가 1인지 확인
        if abs(line[i] - line[i+1]) > 1:
            return False # 차이가 1보다 크면 즉시 실패
            
        # 3. 내리막길 (현재 > 다음)
        if line[i] > line[i+1]:
            target = line[i+1]
            # 길이가 L인지 판단
            for j in range(i + 1, i + 1 + L):
                if j >= N or line[j] != target or visited[j]:
                    return False
                visited[j] = True # 경사로 설치 기록
                
        # 4. 오르막길 (현재 < 다음)
        elif line[i] < line[i+1]:
            target = line[i]
            # 길이가 L인지 판단
            for j in range(i, i - L, -1):
                if j < 0 or line[j] != target or visited[j]:
                    return False
                visited[j] = True # 경사로 설치 기록
                
    return True

    solve()