import sys
sys.stdin = open('input.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    costs = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    N = 13
    dp = [0] * N

    for i in range(1, N):
        dp[i] = costs[0] * plan[i]


    pass