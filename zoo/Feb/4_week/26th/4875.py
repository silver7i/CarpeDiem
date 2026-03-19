dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(sy, sx, N):  # 시작 y, 시작 x, 미로 사이즈 N 을 받아서 3에 도달할 수 있는지 반환
    stack = []  # 스택 생성
    maze[sy][sx] = 1  # 지나간 곳 1로 채우기

    while True:
        for d in range(4):  # 방문할 곳이 있는 지 탐색
            ny, nx = sy + dy[d], sx + dx[d]
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] != 1:  # 다음 위치가 벽이 아니면 아래 실행
                    if maze[ny][nx] == 3:  # 다음 위치가 3이면
                        return 1  # 함수 종료 1(도달 가능) 반환

                    stack.append((sy, sx))  # 다음 위치가 0이면 기존 위치 스택에 푸쉬
                    maze[ny][nx] = 1  # 다음 방문할 곳 1로 채우기
                    sy, sx = ny, nx  # 이동 반영
                    break  # for d 탈출
        else:  # 더 이상 방문할 곳이 없으면
            if stack:  # 스택이 남아 있으면, 이전에 방문했던 곳들이 남아 있으면
                sy, sx = stack.pop()  # 팝해서 위치 갱신
            else:  # 스택도 없으면
                break  # While True 탈출

    # while문을 빠져나왔다는 건 길을 못 찾았다는 뜻이므로 0 반환
    return 0


# 시작 위치 찾는 함수 설정
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


# 실행 부분
t = int(input())

for tc in range(1, t + 1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    sy, sx = find_start(N)
    answer = dfs(sy, sx, N)
    print(f"#{tc} {answer}")
