import sys
sys.stdin = open('input_2566.txt', 'r')
########################################

matrix = [list(map(int, input().split())) for _ in range(9)]
m_len = len(matrix)
max_number = 0
max_xy = (0,0)

for i in range(9):
    for j in range(9):
        if max_number < matrix[i][j]:
            max_number = matrix[i][j]
            max_xy = (i+1, j+1)

print(max_number)
print(*max_xy)

