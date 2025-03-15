import sys
sys.stdin = open('input.txt', 'r')
########################################
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_total = 0

    for i in range(N):
        for j in range(M):
            cnt_val = matrix[i][j]
            for k in range(4):
                for l in range(1, matrix[i][j]+1):
                    ni = i + dx[k] * l
                    nj = j + dy[k] * l
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt_val += matrix[ni][nj]
            if max_total < cnt_val:
                max_total = cnt_val

    print(f"#{tc} {max_total}")


