import sys
sys.stdin = open('input_2116.txt', 'r')
"""
1. 첫번째 주사위의 윗면을 정함
2. 윗면이 정해지면 다음 주사위는 밑면이 정해짐
3. 윗면 밑면을 빼고 옆면에서 가장 큰 수를 저장한다.
4. 1~6 일 때 sum값을 저장하고
5. 거기서 가장 큰 sum값을 print
"""

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]

sum = 0
for i in range(1,7):
    up_number = i # 첫번째 주사위의 윗면을 정함
    for j in range(N):
        if up_number == matrix



