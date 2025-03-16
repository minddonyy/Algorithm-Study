import sys
sys.stdin = open("input.txt", "r")

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def dfs(x, y, count):
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != 1 and complex[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, count+1)



N = int(input())
complex = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
result = []
count = 0

for i in range(N):
    for j in range(N):
        if complex[i][j] or visited[i][j] != 1:
            dfs(i, j, 1)

print(count)