import sys
sys.stdin = open('input.txt', 'r')
########################################

def make_set(x):
    p[x] = x

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())

    p = [0] * (N + 1)
    rank = [0] * (N + 1)

    for i in range(1, N + 1):
        make_set(i)


    for _ in range(M):
        p, n = map(int, input().split())
