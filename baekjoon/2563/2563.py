import sys
sys.stdin = open("input.txt", "r")

white_length = 100
white = [[0]* 100 for _ in range(white_length)]

N = int(input())
for _ in range(N):
