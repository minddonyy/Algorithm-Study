import sys
sys.stdin = open("input_1933.txt", "r")

N = int(input())

for number in range(1,N+1):
    if N % (number) == 0:
        print(number, end= " ")