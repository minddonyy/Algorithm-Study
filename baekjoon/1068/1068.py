import sys
sys.stdin = open("input.txt", "r")

def dfs(v):
    tree[v] = -2
    for i in range(N):
        if v == tree[i]:
            dfs(i)

N = int(input())
tree = list(map(int, input().split()))
delete_node_idx = int(input())

dfs(delete_node_idx)
result = 0

for i in range(N):
    if tree[i] != -2 and i not in tree:
        result+=1

print(result)