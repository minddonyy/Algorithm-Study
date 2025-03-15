N = 5
matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]

main_diagonal_sum = 0
# for i in range(N):
#     main_diagonal_sum += matrix[i][i]

for i in range(N):
    for j in range(N):
        if i == j:
            main_diagonal_sum+=matrix[i][j]


sub_diagonal_sum = 0

for i in range(N):
    for j in range(N):
        if i == N - i -j:
            sub_diagonal_sum+= matrix[i][j]

# for i in range(N):
#     main_diagonal_sum += matrix[i][N-1-i]

middle_value = matrix[N//2][N//2]

total_diagonal_sum = main_diagonal_sum +sub_diagonal_sum - middle_value
print(total_diagonal_sum)
