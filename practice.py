import math

#두 점의 위치
start = (2, 0)
target = (2,-2)


x = target[0] - start[0]
y = target[1] - start[1]

# radian = math.atan(y/x)
radian = math.atan2(y,x)

print(radian)
theta = math.degrees(radian)
print(theta)