import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")


def dfs(x):
    visited[x] = 1
    for node in list[x]:
        if not visited[node]:
            dfs(node)

N, M = map(int, sys.stdin.readline().split())
list = [[] for _ in range(N+1)]
visited = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    list[a].append(b)
    list[b].append(a)


result = 0
for i in range(1, N+1):
    if not visited[i]:
        result += 1
        dfs(i)

print(result)