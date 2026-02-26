"""
[일타싸피 클리어 전략]
1. 타겟 선정: 선공/후공 여부에 따라 남은 공 중 최우선 순위의 공을 찾습니다.
2. 최적홀 탐색: 피타고라스 정리를 이용해 타겟 공과 가장 가까운 홀을 찾습니다.
3. 고스트볼 조준: 목적구를 홀에 넣기 위해, 홀 반대편으로 공 지름만큼 떨어진 가상의 타격점(고스트볼)을 계산합니다.
4. 각도 및 힘 계산: 삼각함수(atan2)를 이용해 타격 각도를 구하고, 남은 거리에 비례하여 파워를 조절합니다.
"""

# 내 위치 설정
BALL_RADIUS = 5.74 / 2  # 공의 반지름 (고스트볼 계산 시 공 지름만큼 띄우기 위해 필요)
white_x, white_y = balls[0][0], balls[0][1]  # 흰 공의 현재 x, y 좌표 저장

# 타겟 설정
# 내가 선공(1)이면 1,3,5번 공을, 후공(2)이면 2,4,5번 공을 노리도록 순서 지정
target_indices = [1, 3, 5] if order == 1 else [2, 4, 5]
target_ball_idx = -1  # 아직 칠 공을 못 찾았다는 의미로 -1 초기화

# 노려야 할 공들을 순서대로 확인
for idx in target_indices:
    if balls[idx][0] != -1:  # 해당 공의 x좌표가 -1이 아니면 (즉, 아직 당구대 위에 남아있다면)
        target_ball_idx = idx  # 이 공을 타겟으로 확정하고
        break  # 타겟을 찾았으니 반복문 종료

# 칠 공이 하나라도 남아있을 때만 아래 당구 물리 로직 실행
if target_ball_idx != -1:
    target_x, target_y = balls[target_ball_idx][0], balls[target_ball_idx][1]  # 확정된 타겟 공의 좌표 저장

    # 최적홀 찾기
    best_hole = HOLES[0]  # 가장 가까운 홀의 좌표를 담을 변수
    min_dist_to_hole = float('inf')  # 최소 거리를 비교하기 위해 처음엔 무한대(inf)로 설정

    # 6개의 홀을 하나씩 꺼내서 확인
    for hole in HOLES:
        # 피타고라스 정리를 사용하여 타겟 공과 현재 홀 사이의 직선 거리 계산
        dist = math.sqrt((hole[0] - target_x) ** 2 + (hole[1] - target_y) ** 2)
        
        if min_dist_to_hole > dist:  # 지금 계산한 거리가 기존 최소 거리보다 짧다면
            min_dist_to_hole = dist  # 최소 거리를 갱신
            best_hole = hole  # 최적의 홀 위치를 갱신

    # 고스트볼 설정
    # 목적구에서 최적 홀을 향하는 방향의 비율(단위 벡터)을 계산
    dx = (best_hole[0] - target_x) / min_dist_to_hole
    dy = (best_hole[1] - target_y) / min_dist_to_hole

    # 목적구 위치에서 홀 반대 방향(-)으로 공 지름(2 * R)만큼 떨어진 '고스트볼(실제 타격점)' 좌표 계산
    ghost_x = target_x - dx * (2 * BALL_RADIUS)
    ghost_y = target_y - dy * (2 * BALL_RADIUS)

    # 각도 설정
    # 아크탄젠트를 사용하여 내 공에서 고스트볼을 바라보는 각도를 라디안으로 계산
    radian = math.atan2(ghost_x - white_x, ghost_y - white_y)
    angle = math.degrees(radian)  # 라디안 값을 일반 각도(도, Degree)로 변환

    if angle < 0:  # 계산된 각도가 음수일 경우
        angle += 360  # 360도를 더해 양수 방향으로 보정
    
    # 힘 설정
    # 내 공에서 고스트볼까지의 직선 거리를 계산
    dist_to_ghost = math.sqrt((ghost_x - white_x) ** 2 + (ghost_y - white_y) ** 2)

    # 전체 이동 거리(내공~고스트볼 + 목적구~홀)에 0.6배를 하여 적절한 파워 설정
    power = (dist_to_ghost + min_dist_to_hole) * 0.6

    if power > 100:  # 파워가 게임 시스템의 최대치(100)를 넘지 않도록 안전장치 설정
        power = 100