import sys
from collections import deque
sys.stdin = open("input_1226.txt", "r")


dxy = [[0,-1], [0,1], [-1, 0], [1, 0]]
def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited = [[0] * N for _ in range(N)]

    while queue:
        x, y = queue.popleft() # 첫번째 좌표를 뺀다
        if maze[x][y] == 3:
            return 1
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y # 다음 좌표값
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and maze[nx][ny] != 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return 0
T = 10
for tc in range(1, T+1):
    tase_case = int(input())
    N = 16 # 미로의 x, y 길이
    maze = [list(map(int, input().strip())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                result = bfs(i, j)

    print(f"#{tase_case}", result)