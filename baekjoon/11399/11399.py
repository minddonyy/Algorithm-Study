"""
3 1 4 3 2
4
8
11
13

"""

N = int(input())
p_list = list(map(int, input().split())) # 인출하는데 걸리는 시간

sum_list = []
total = 0
result =0
for i in range(len(p_list)):
    total += p_list[i]
    sum_list.append(total)

for j in range(len(sum_list)):
    print(sum_list[j])
    result+=sum_list[j]

print(result)

