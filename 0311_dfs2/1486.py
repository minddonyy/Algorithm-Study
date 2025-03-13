import sys
sys.stdin = open("input_1486.txt", "r")

def dfs(idx, h_sum):
    global result
    if h_sum >= result:
        return
    if idx == N:
        if h_sum >= B:
            result = min(result, h_sum)
        return

    dfs(idx+1, h_sum + height_list[idx])
    dfs(idx+1, h_sum)

T = int(input())
for tc in range(1, T+1):
    N,B = map(int, input().split())
    height_list = list(map(int, input().split()))
    result = 10000 * N # 최대값

    dfs = (0,0)

    print(f"#{tc} {result-B}")




