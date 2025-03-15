import sys
sys.stdin = open("input_2025.txt", "r")

N = int(input())
total_sum = 0
i = 0
while i <= N:
    total_sum+=i
    i+=1

#
# for number in range(N):
#     total_sum+=int(number+1)

print(total_sum)