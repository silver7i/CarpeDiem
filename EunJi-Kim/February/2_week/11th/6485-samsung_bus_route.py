import sys
from pathlib import Path

file_path = Path(__file__).resolve().parents[3] / "input_src" / f"{Path(__file__).stem}.txt"
file_path.touch(exist_ok=True)

sys.stdin = open(file_path, "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    # i 번째 버스 노선은 Ai 이상이고, Bi 이하인 모든 정류장만 Ai<=i<=Bi
    AtoB_arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())    # P => 버스 정류장 개수
    Cj = [int(input()) for _ in range(P)] # Cj => j는 버스 노선의 개수

    #route_cnt = [0 for _ in range(P+1)] # 이 식으로 하면 런타임 에러 뜸
    route_cnt = [0] * 5001

    for a, b in AtoB_arr:
        for i in range(a, b+1):
            route_cnt[i] += 1
            
    # P개의 각 정류장에 몇 개의 버스 노선이 다니는지 출력
    # 출력할 P개의 정수 중 j번째는 Cj번 버정을 지나는 버스 노선의 개수
    print(f'#{test_case}', end=' ')
    for i in range(P):
        print(route_cnt[Cj[i]], end=' ') 
    print()
