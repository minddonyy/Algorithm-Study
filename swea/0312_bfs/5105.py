import sys
from collections import deque
sys.stdin = open("input_5105.txt", "r")
"""
벽 체크, visited 체크, 델타, 델타의 범위
"""
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
def bfs(x, y):
    queue = deque()
    queue.append((x,y,0))

    while queue:
        x,y,depth = queue.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if not(0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny] == 1:
                continue
            if maze[nx][ny] == 1:
                continue
            if maze[nx][ny] == 3:
                return depth

            visited[nx][ny] = 1
            queue.append((nx,ny,depth+1))

    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input().strip())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                minsun = bfs(i, j)


    print(f"#{tc}", minsun)