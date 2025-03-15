import sys
sys.stdin = open('input.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    # N : 배열의 크기, M : 파리채의 크기
    N, M = map(int,input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]


    kill_flies = 0

    #파리채만큼의 범위를 확보하기 위해서
    for i in range(N - M +1):
        for j in range(N - M +1):
            tmp_sum = 0 # (i, j)가 이동할 때마다 매번 초기화해서 다시 죽인 파리수를 구해야 함.
            for m in range(M):
                for n in range(M):
                    tmp_sum = grid[i+m][j+n]
            #파리채 영역만큼 다 더해주고 다시 도달
            kill_flies = max(kill_flies, tmp_sum)


    print(f"#{tc} {kill_flies}")