import sys
sys.stdin = open("input.txt", "r")

N = int(input()) # 도시의 개수
load = list(map, int(input().split())) # 도시를 잇는 도로의 길이
price = list(map, int(input().split()))

for i in range(N):
    pass