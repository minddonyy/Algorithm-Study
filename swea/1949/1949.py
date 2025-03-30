import sys
sys.stdin = open("input.txt", "r")

def find_high():
    for i in range(N):
        for j in range(N):
            pass


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    hiking_map = [list(map(int, input().split())) for _ in range(N)]

