import sys
sys.stdin = open('input_2309.txt', 'r')
########################################


heights = [int(input()) for _ in range(9)]
total_sum = sum(heights)

for i in range(len(heights)):
    for j in range(i+1, len(heights)):
        if total_sum - (heights[i] + heights[j]) == 100:
            result_dwarf = [heights[k] for k in range(9) if k != i and k != j]


result_dwarf.sort()
for d in result_dwarf:
    print(d)



