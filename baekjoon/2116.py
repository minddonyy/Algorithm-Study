import sys
sys.stdin = open('input_2116.txt', 'r')
"""
1. 첫번째 주사위의 윗면을 정함
2. 윗면이 정해지면 다음 주사위는 밑면이 정해짐
3. 윗면 밑면을 빼고 옆면에서 가장 큰 수를 저장한다.
4. 1~6 일 때 sum값을 저장하고
5. 거기서 가장 큰 sum값을 print
"""
def find_bottom(top, dice):
    pairs = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
    top_index = dice.index(top)  #
    bottom_index = pairs[top_index]
    return dice[bottom_index]

def find_side():
    pass
N = int(input())
dice = [list(map(int,input().split())) for _ in range(N)]
max_value = 0
result = 0

for i in range(6):
    top = dice[0][i]
    bottom_value = find_bottom(top, dice[0])
    total_sum = 0
    side_value = max([x for x in dice[0] if x not in (top, bottom_value)])
    total_sum = side_value
    for j in range(1, N):
        bottom_value = top
        top = find_bottom(bottom_value, dice[j])
        side_value = max([x for x in dice[j] if x not in (top, bottom_value)])
        total_sum+=side_value
    result = max(result, total_sum)

print(result)









