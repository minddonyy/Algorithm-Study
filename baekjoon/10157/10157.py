
C,R = map(int, input().split())
K = int(input())

dx, dy = [1,0,-1,0], [0,1, 0, -1]


if R*C < K:
    print(0)
else:
    seat_matrix = [[0] * C for _ in range(R)]
    ci, cj, dr = 0, 0, 0
    for n in range(1, K+1):
        seat_matrix[ci][cj] = n
        if n == K:
            print(cj + 1, ci + 1)
            break
        nx, ny = ci + dx[dr], cj + dy[dr]
        if  0 <= nx < R and 0 <= ny < C and seat_matrix[nx][ny] == 0:
            ci, cj = nx, ny
        else:
            dr = (dr + 1) % 4
            ci, cj = ci + dx[dr], cj + dy[dr]
