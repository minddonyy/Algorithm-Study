import sys
sys.stdin = open('input.txt', 'r')
########################################

T = 10   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    row_max = 0
    for row in arr:
        row_sum = sum(row)
        if row_sum > row_max:
            row_max = row_sum

    col_max = 0
    for col in zip(*arr):
        col_sum = sum(col)
        if col_sum > col_max:
            col_max = col_sum

    diagonal_sum1 = 0
    diagonal_sum2 = 0 #대각선의 합
    diagonal_max = 0

    for i in range(100):
        diagonal_sum1 += arr[i][i]
        diagonal_sum2 += arr[i][99-i]
        diagonal_max = max(diagonal_sum1, diagonal_sum2)


    print(f"#{tc_num} {max(row_max,col_max,diagonal_max)}")


