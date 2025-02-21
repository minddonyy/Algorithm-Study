#점이 4개가 있는데 두번째로 가까운 점의 거리와 각도를 구하는 코드
import math

Ax, Ay = 0,0
points = [
    (1,2), (-2,-3), (3,1), (-1,4)
]

distance_list = [] #계산된 거리를 저장
# 각 점별로 거리를 계산
for Tx, Ty in points:
    x = Tx - Ax # x축의 거리
    y = Ty - Ay # y축의 거리
    r = math.sqrt(x**2 + y**2) # distance
    radian = math.atan2(y,x)
    angle = math.degrees(radian) #각도 정보

    distance_list.append((r,angle))

distance_list.sort()
print(distance_list[1])
