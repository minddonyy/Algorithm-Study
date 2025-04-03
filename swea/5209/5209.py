import sys
sys.stdin = open("input.txt", "r")

def calc_min(idx, c_sum):
    global min_result

    if min_result < c_sum: # 가지치기.. 이거 안 해줘서 런타임 뜸
        return

    if idx == N:
        min_result = min(min_result, c_sum) # 최소값 갱신
        return

    for j in range(N): # 2차원 배열 돌면서
        if visited[j] != 1: # 방문하지 않은 곳이라면
            visited[j] = 1 #방문처리해주고
            calc_min(idx+1, c_sum + factory[idx][j]) #재귀적으로 들어간다
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int,input().split())) for _ in range(N)]

    min_result = 99999999
    visited = [0] * N

    calc_min(0, 0)

    print(f"#{tc}", min_result)