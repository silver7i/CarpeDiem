# 여기서부터 코드를 작성하세요.

# 1. 내 공(흰 공) 위치 파악
BALL_RADIUS = 5.74 / 2  # 당구공의 반지름
white_x = balls[0][0]
white_y = balls[0][1]

# 2. 어떤 공을 칠지 결정하기
# 내가 선공(1)이면 1, 3, 5번 / 후공(2)이면 2, 4, 5번을 노린다
target_indices = [1, 3, 5] if order == 1 else [2, 4, 5]
target_ball_idx = -1

# 노려야 할 공 중에서, 아직 당구대 위에 있는(-1이 아닌) 첫 번째 공 찾기
for idx in target_indices:
    if balls[idx][0] != -1: 
        target_ball_idx = idx
        break

# 칠 공이 남아있을 때만 아래의 당구 계산을 시작한다
if target_ball_idx != -1:
    target_x = balls[target_ball_idx][0]
    target_y = balls[target_ball_idx][1]

    # 3. 6개의 구멍(Hole) 중 목적구와 가장 가까운 구멍 찾기
    best_hole = HOLES[0]
    min_dist_to_hole = float('inf') # 처음엔 거리를 무한대로 설정
    
    for hole in HOLES:
        # 피타고라스 정리: 공과 구멍 사이의 직선거리 구하기
        dist = math.sqrt((hole[0] - target_x)**2 + (hole[1] - target_y)**2)
        if dist < min_dist_to_hole:
            min_dist_to_hole = dist
            best_hole = hole

    # 4. 고스트볼(진짜로 조준해야 할 타격 지점) 좌표 계산
    # 목적구에서 구멍 방향으로의 비율(단위 벡터) 구하기
    dx = (best_hole[0] - target_x) / min_dist_to_hole
    dy = (best_hole[1] - target_y) / min_dist_to_hole
    
    # 목적구 위치에서 구멍 반대편으로 공 지름(2R)만큼 떨어진 좌표가 고스트볼!
    ghost_x = target_x - dx * (BALL_RADIUS * 2)
    ghost_y = target_y - dy * (BALL_RADIUS * 2)

    # 5. 칠 각도(Angle) 계산
    # 내 공에서 고스트볼을 향하는 각도를 아크탄젠트로 계산
    radian = math.atan2(ghost_x - white_x, ghost_y - white_y)
    angle = math.degrees(radian)
    
    # 각도가 마이너스로 나오면 360도를 더해서 플러스로 바꿔줌
    if angle < 0:
        angle += 360

    # 6. 칠 세기(Power) 계산
    # 내 공에서 고스트볼까지의 거리 계산
    dist_to_ghost = math.sqrt((ghost_x - white_x)**2 + (ghost_y - white_y)**2)
    
    # 쳐야 할 전체 거리(내공~고스트볼 + 목적구~구멍)에 0.6배를 해서 파워 결정
    power = (dist_to_ghost + min_dist_to_hole) * 0.6
    if power > 100: 
        power = 100