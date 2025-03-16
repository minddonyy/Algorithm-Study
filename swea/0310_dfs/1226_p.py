import sys
sys.stdin = open("input_1226.txt", "r")
from collections import deque

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
def find_three(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        start_x, start_y = queue.popleft()

        if maze[start_x][start_y] == 3:
            return 1

        for dx, dy in dxy:
            nx = start_x + dx
            ny = start_y + dy

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]!= 1 and maze[nx][ny] != 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return 0



T= 10
for tc in range(1, T+1):
    test_case = int(input())
    n = 16
    maze = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                result = find_three(i, j)

    print(f"#{test_case}", result)
