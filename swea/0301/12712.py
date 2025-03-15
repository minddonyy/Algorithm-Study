import sys
sys.stdin = open("input_12712.txt", "r")
"""
파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다. 
스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다.
스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
다음은 M=3 세기로 스프레이를 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다. 뿌려진 일부가 영역을 벗어나도 상관없다.
"""

# + 로 분사됐을 때
def get_plus_area(matrix,N, M):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    max_kill = 0

    for i in range(N):
        for j in range(N):
            cur_value = matrix[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + dx[k] * l
                    nj = j + dy[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        cur_value += matrix[ni][nj]
            max_kill = max(max_kill, cur_value)
    return max_kill

# x로 분사됐을 때
def get_x_area(matrix, N, M):
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]
    max_kill = 0

    for i in range(N):
        for j in range(N):
            cur_value = matrix[i][j]
            for k in range(4):
                for l in range(1, M):
                    ni = i + dx[k] * l
                    nj = j + dy[k] * l
                    if 0 <= ni < N and 0 <= nj < N:
                        cur_value += matrix[ni][nj]
            max_kill = max(max_kill, cur_value)
    return max_kill


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    x_area = get_x_area(matrix,N,M)
    plus_area = get_plus_area(matrix, N,M)

    print(f"#{tc}", max(x_area, plus_area))