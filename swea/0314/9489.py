import sys
sys.stdin = open("input_9489.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    for i in range(N):
        count = 0
        for j in range(M):
            if matrix[i][j] == 1:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                count = 0

    for i in range(M):
        count = 0
        for j in range(N):
            if matrix[j][i] == 1:
                count+=1
                if max_count < count:
                    max_count = count
            else:
                count = 0

    print(f"#{tc}", max_count)


