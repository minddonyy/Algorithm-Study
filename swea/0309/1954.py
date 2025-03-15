import sys
sys.stdin = open("input_1954.txt", "r")

T = int(input())
# 이동방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    i, j, cnt, dr = 0, 0, 1, 0
    matrix[i][j] = cnt

    while cnt <= N*N:
        ni = i + dx[dr]
        nj = j + dy[dr]
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 0:
            i, j = ni, nj
            matrix[i][j] = cnt
            cnt+=1
        else:
            dr = (dr+1) % 4


    print(f"#{tc}")
    for l in matrix:
        print(*l)