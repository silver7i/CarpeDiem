import math
from pprint import pprint

ground = [[0] * 21 for _ in range(51)]

holes = [[0,0], [0, 20], [50, 20], [50, 0]]
target_ball = [40, 10]
my_ball = [20, 5]

for x, y in holes:
    ground[x][y] = 3

ground[target_ball[0]][target_ball[1]] = 2
ground[my_ball[0]][my_ball[1]] = 1


### 삼각함수
a = abs(target_ball[0]-my_ball[0])
b = abs(target_ball[1]-my_ball[1])

r = math.sqrt(a**2 + b**2)
radian = math.atan(b/a)
degree = math.degrees(radian)
print(a, b, r, degree)

### 벽 맞고 이동

def calculate_theta(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 + y1
    tan_theta = a/b
    theta = math.atan(tan_theta)
    print(a, b, theta)
    return theta

calculate_theta(my_ball[0], my_ball[1], target_ball[0], target_ball[1])

### 접점으로 공 보내기





pprint(ground)