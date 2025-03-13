import sys
sys.stdin = open("input_4875.txt", "r")
"""
1은 벽, 0은 길, 2는 출발점, 3은 도착점

1. maze를 돌면서 2의 좌표값을 찾는다
2. 좌표값을 저장한다
3. 델타 탐색으로 상하좌우를 본다
4. 주변에 1이 아닐 때를 찾고 탐색한다
5. 3일 때는 return 1을 반환한다
"""
def dfs(start_x, start_y):

    if maze[start_x][start_y] == 3: # 3일 때는 return 1일 반환한다
        return 1

    for dx, dy in dxy:
        # 다음 좌표값 지정
        next_x = start_x + dx
        next_y = start_y + dy

        if 0 <= next_x < n and 0 <= next_y < n and visited[next_x][next_y] != 1:
            visited[next_x][next_y] = 1
            if dfs(next_x, next_y):
                return 1

    return 0

T = int(input())
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
for tc in range(1, T+1):
    n = int(input())
    maze = [list(map(int, input().strip())) for _ in range(n)]

    visited = [[0]*n for _ in range(n)] #visited 배열
    result = 0
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                result = dfs(i, j)


    print(f"#{tc}", result)