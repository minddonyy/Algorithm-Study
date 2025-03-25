import sys
sys.stdin = open("input.txt", "r")

"""

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
"""
from collections import deque
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
def bfs(x, y, cnt = 1):
    min_cnt = 999999999
    queue = deque()
    queue.append((x, y, cnt))

    while queue:
        start_x, start_y, cnt = queue.popleft()

        if (start_x == N-1) and (start_y == M-1):
            if min_cnt > cnt:
                min_cnt = cnt
            return min_cnt

        for dx, dy in dxy:
            nx = start_x + dx
            ny = start_y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 1:
                    continue
                if maze[nx][ny] == 0:
                    continue
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt+1))

    return cnt


N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
result = bfs(0, 0)

print(result)
