import sys
sys.stdin = open("input.txt", "r")
from collections import deque
M,N,K = map(int, input().split())
paper = [[0]*N for _ in range(M)]

dxy = [[0,1], [0,-1], [1,0], [-1, 0]]
visited = [[0]*N for _ in range(M)]
result = []

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    count = 1

    while queue:
        q_x, q_y = queue.popleft()

        for dx, dy in dxy:
            nx = dx + q_x
            ny = dy + q_y

            if 0 <= nx < M and 0 <= ny < N:
                if visited[nx][ny] !=1 and paper[nx][ny] != 1:
                    queue.append((nx, ny))
                    count += 1
                    visited[nx][ny] = 1

    result.append(count)



for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if paper[i][j] == 0:
                paper[i][j] +=1

for k in range(M):
    for l in range(N):
        if paper[k][l] != 1 and visited[k][l] != 1:
            bfs(k, l)
#
# bfs(0, 0)
result.sort()
print(len(result))
print(*result)




