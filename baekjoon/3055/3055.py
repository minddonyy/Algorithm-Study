from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def find_b(start_x, start_y, cnt=0):
    min_cnt = 9999999
    queue = deque()
    queue.append((start_x, start_y, cnt))
    visited[start_x][start_y] = 1

    while queue:
        x, y, cnt = queue.popleft()

        if forest[x][y] == 'S':
            if min_cnt > cnt:
                min_cnt = cnt
            return min_cnt

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < R and 0 <= ny < C:
                if visited[nx][ny]!=1 and forest[nx][ny] != '*':
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = 1

    return "KAKTUS"


R, C = map(int, input().split())
forest = [list(input().strip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
result = 0

for i in range(R):
    for j in range(C):
        if forest[i][j] == 'D':
            result = find_b(i,j)

print(result)