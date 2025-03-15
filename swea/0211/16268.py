import sys
sys.stdin = open('input_16268.txt', 'r')
########################################

dx = [0, 0,-1,1]
dy = [-1,1,0,0]
T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N,M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(matrix)
    max_value = 0

    for i in range(N):
        for j in range(M):
            cur_value = matrix[i][j]
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if 0 <= ni < N and 0 <= nj < M:
                    cur_value += matrix[ni][nj]

            max_value = max(max_value, cur_value)

    print(f"#{tc} {max_value}")