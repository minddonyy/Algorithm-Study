import sys
sys.stdin = open("input.txt", "r")

N = int(input())
numbers = list(map(int,input().split()))

count = 1
max_count = 1
for i in range(N-1):
    if numbers[i+1] >= numbers[i]:
        count += 1
    else:
        count = 1

    if max_count < count:
        max_count = count

count = 1
for j in range(N-1):
    if numbers[j+1] <= numbers[j]:
        count +=1
    else:
        count = 1

    if max_count < count:
        max_count = count

print(max_count)





