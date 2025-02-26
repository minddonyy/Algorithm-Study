import sys
sys.stdin = open('input_9490.txt', 'r')
########################################
dxy = [[-1, 0], [1, 0], [0,1], [0,-1]]

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0
    for i in range(N):
        for j in range(M):
            cur_val = matrix[i][j]
            for dx, dy in dxy:
                for k in range(1, matrix[i][j]+1):
                    ni = i + dx * k
                    nj = j + dy * k

                    if 0 <= ni < N and 0 <= nj < M:
                        cur_val += matrix[ni][nj]
                    else:
                        break

            max_val = max(max_val, cur_val)


    print (f"#{tc} {max_val}")





