import sys
sys.stdin = open("input_11315.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pan = [list(map(str, input())) for _ in range(N)]
    result = "NO"

    for i in range(N):
        for j in range(N):
            pass
