import sys
sys.stdin = open('input.txt', 'r')
########################################

def calc_battery(idx, b_sum, current):
    global min_battery

    if min_battery < b_sum:
        return

    if idx == N-1:
        min_battery = min(min_battery, b_sum + zido[current][0])
        return

    for j in range(N):
        if not visited[j]:
            visited[j] = 1
            calc_battery(idx+1, b_sum+zido[current][j], j)
            visited[j] = 0

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    zido = [list(map(int, input().split())) for _ in range(N)]

    min_battery = 999999
    visited = [0] * N

    visited[0] = 1

    calc_battery(0, 0, 0)

    print(f"#{tc}", min_battery)