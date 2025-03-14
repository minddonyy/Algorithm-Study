import sys
from collections import deque
sys.stdin = open("input_1227.txt", "r")
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            # 벽 체크
            if maze[nx][ny] == 1:
                continue
            # 범위 체크
            if not(0 <= nx < N and 0 <= ny < N):
                continue
            # visited 체크
            if visited[nx][ny] == 1:
                continue
            if maze[nx][ny] == 3:
                return 1

            queue.append((nx, ny))
            visited[nx][ny] = 1

    return 0


T = 10
for tc in range(1, T+1):
    N = 100
    test_case = int(input())
    maze = [list(map(int,input().strip())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                result = bfs(i, j)

    print(f"#{test_case}", result)