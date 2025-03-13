import sys
sys.stdin = open("input_2819.txt", "r")
"""
(0,0)부터 matrix에 동서남북(상하좌우) 네방향으로 인접한 격자로 총 여섯 번 이동
각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리 수

1. (0,0)에서부터 동서남북 탐색을 한다
1-1. 동서남북으로만 가는 게 아니라 쭉쭉 뻗어나갈 수 있음
2. 
"""
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
def dfs(start_x, start_y, cnt, array):
    if cnt == 6:
        result.add(array)
        return

    for dx, dy in dxy:
        nx = dx + start_x
        ny = dy + start_y
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, cnt+1, array+str(matrix[nx][ny]))

T = int(input())
for tc in range(1, T+1):
    N = 4
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = set()
    cnt = 0

    for i in range(N):
        for j in range(N):
            dfs(i, j, cnt, str(matrix[i][j]))

    print(f"#{tc}", len(result))