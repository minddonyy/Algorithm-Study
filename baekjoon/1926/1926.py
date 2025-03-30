from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    count = 1

    while queue:
        x1, y1 = queue.popleft()

        for dx, dy in dxy:
            nx = dx + x1
            ny = dy + y1

            if 0 <= nx < height and 0 <= ny < width:
                if visited[nx][ny] != 1 and white_board[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    count+=1

    result.append(count)

height, width = map(int, input().split())
white_board = [list(map(int, input().split())) for _ in range(height)]

visited = [[0] * width for _ in range(height)]
result = []

for i in range(height):
    for j in range(width):
        if white_board[i][j] and visited[i][j]!=1:
            bfs(i, j)


result.sort()
print(len(result))
if len(result) == 0:
    print(0)
else:
    print(max(result))