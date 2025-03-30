import sys
sys.stdin = open("input.txt", "r")

from collections import deque
dxy =[[-1, -1], [-1, 0], [-1, 1], [0,- 1], [0, 1], [1, -1], [1, 0], [1, 1]]
def popping(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and pop_map[nx][ny] != '*':
                    visited[nx][ny] = 1
                    change_popping(nx, ny)
                    

def change_popping(x, y):
    cnt = 0
    visited[x][y] = 1
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if pop_map[nx][ny] == '*':
                cnt+=1

    if cnt == 0:
        popping(x, y)


def count_popping(x, y):
    cnt = 0
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and pop_map[nx][ny] == '*':
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pop_map = [list(map(str, input().strip())) for _ in range(N)]
    visited = [[0]* N for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and pop_map[i][j]!= '*' and count_popping(i, j) == 0:
                popping(i, j)
                cnt +=1

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and pop_map[i][j] != '*':
                visited[i][j] = 1
                cnt += 1

    print(f"#{tc}", cnt)



