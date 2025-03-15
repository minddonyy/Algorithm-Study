import sys
sys.stdin = open('input_18123.txt', 'r')
########################################
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_sum = 0

    for i in range(N):
        for j in range(N):
            cur_value = arr[i][j]
            for k in range(4):
                ni, nj = i+dx[k], j+dy[k]

                if 0 <= ni < N and 0 <= nj < N:
                    total_sum += abs(cur_value-arr[ni][nj])

    print(f"#{tc} {total_sum}")