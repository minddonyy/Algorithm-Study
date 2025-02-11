import sys
sys.stdin = open('input.txt', 'r')
########################################
#  델타 탐색 순서 중요 x
dxy= [[0,1],[0,-1],[1,0],[-1,0]]
T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_value = 0

    for i in range(N):
        for j in range(M):
            sum_val = arr[i][j]

            for dx, dy in dxy:
                for dist in range(1, arr[i][j]+1):
                    # 델타에 퍼져나가는만큼 곱해져서 이동한다
                    # dist는 1부터 시작, 거리가 멀어질수록 이동거리가 늘어난다
                    ni = i + dx * dist
                    nj = j + dy * dist

                    # 범위가 벗어나면, 더 이상 탐색 중지
                    # if 0> ni or ni>= N or 0 >nj or nj >= M:
                    #     break
                    #
                    #  sum_val += arr[ni][nj]

                    if 0 <= ni < N and 0 <= nj < M:
                        sum_val += arr[ni][nj]
                    else:
                        break
            # 여기까지 왔다는 건 다 더했다.
            max_value = max(max_value, sum_val)
    print(f'#{tc} {max_value}')