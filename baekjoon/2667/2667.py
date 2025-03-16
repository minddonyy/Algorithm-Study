import sys
sys.stdin = open("input.txt", "r")
from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def find_complex(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    count = 1

    while queue:
        x1, y1 = queue.popleft()

        for dx,dy in dxy:
            nx = dx+ x1
            ny = dy + y1

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] != 1 and matrix[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                count +=1

    result.append(count)



N = int(input())
matrix = [list(map(int,input().strip())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] and visited[i][j] != 1:
            find_complex(i, j)


result.sort()
print(len(result))
print(*result, sep='\n')

