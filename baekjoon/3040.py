import sys
sys.stdin = open('input_3040.txt', 'r')
########################################

heights = [int(input()) for _ in range(9)]

total_sum = sum(heights)

for i in range(len(heights)):
    for j in range(i+1, len(heights)):
        if total_sum - (heights[i]+heights[j]) == 100:
            result = [heights[k] for k in range(9) if i!=k and j!=k]

for r in result:
    print(r)