arr = list(range(10))
n = len(arr)
subset_cnt = 2 ** n

subsets = []
for i in range(subset_cnt):
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])

    subsets.append(subset)

for subset in subsets:
    if sum(subset) == 10:
        print(subset)
