import sys
sys.stdin = open('input_2001.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    max_count = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            count = 0
            for n in range(M):
                for m in range(M):
                    count += matrix[i+n][j+m]

            max_count = max(max_count, count)

    print(f"#{tc} {max_count}")
