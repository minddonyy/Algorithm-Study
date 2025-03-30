import sys
sys.stdin = open("input.txt", "r")

def dfs(x, count):
    visited[x] = 1
    for node in network[x]:
        if not visited[node]:
            count = dfs(node, count+1)
    return count

N = int(input())
M = int(input())
network = [[] for _ in range(N+1)]
visited = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

print(dfs(1,0))





