import sys
sys.stdin = open("input_23795.txt","r")

def check_beam(alien, matrix):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for k in range(4):  # 4방향 탐색
        # 빔은 끝까지 나간다
        for i in range(1, N):
            nr = alien[0] + (dr[k] * i)
            nc = alien[1] + (dc[k] * i)

            if 0 <= nr < N and 0 <= nc < N:
                if matrix[nr][nc] == 1:  # 빔이 벽을 만나면 해당 방향에 대한 빔 발사 종료
                    break
                matrix[nr][nc] += 28  # 빔이 스친 곳을 표시하자 (28은 28일이라)

    return matrix

def get_safe_area(matrix):
    count = 0
    for row in range(N):
        for col in range(N):
            if matrix[row][col] == 0:
                count+=1

    return count


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    alien = None
    for row in range(N):
        for col in range(N):
            if matrix[row][col] == 2:
                alien = (row, col)

    matrix = check_beam(alien, matrix)
    result = get_safe_area(matrix)

    print(f"#{tc} {result}")






