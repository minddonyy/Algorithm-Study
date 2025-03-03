import sys
sys.stdin = open("input_11039.txt", "r")
'''
1. 1 의 위치 좌표를 찾자
     해당 위치에서 가로의 길이를 계산한다
     해당 위치에서 세로의 길이를 계산한다
2. 가로와 세로의 길이의 곱을 구한다
3. 곱의 결과가 최대 값인지 확인한다

처음부터 반복한다
'''


def get_horizontal_length(row, col):
    horizontal = 0
    for j in range(col, N):
        if matrix[row][j] == 0:
            break
        horizontal += 1

    return horizontal


def get_vertical_length(row, col):
    vertical = 0
    for i in range(row, N):
        if matrix[i][col] == 0:
            break
        vertical += 1

    return vertical


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_rectangle = 0
    for i in range(N):
        for j in range(N):
            cur_rectangle = 0
            if matrix[i][j] == 1:
                # 가로의 길이를 찾아야 함
                horizontal = get_horizontal_length(i,j)
                # 세로의 길이를 찾아야 함
                vertical = get_vertical_length(i,j)
                # 넓이를 구한다
                cur_rectangle = (horizontal * vertical)

            # 가장 큰 값을 구해야 함
            max_rectangle = max(max_rectangle, cur_rectangle)

    print(f"#{tc} {max_rectangle}")





