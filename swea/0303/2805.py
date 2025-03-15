import sys
sys.stdin = open("input_2805.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    total_sum = 0
    for i in range(N):
        start = abs(N // 2 - i)
        end = N - abs(N // 2 - i)

        for j in range(start, end):
            total_sum += matrix[i][j]

    print(f"#{tc}", total_sum)

