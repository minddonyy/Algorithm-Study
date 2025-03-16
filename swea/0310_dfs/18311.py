import sys
sys.stdin = open("input_18311.txt", "r")
def dfs(current):
    result.append(current)
    visited[current] = True
    for i in range(len(adj_matrix)):
        if adj_matrix[current][i] and not visited[i]:
            dfs(i)

V, E = map(int, input().split()) #  정점의 개수, 간선의 개수
edge = list(map(int, input().split()))
adj_matrix = [[0]*(V+1) for _ in range(V+1)]
visited = [False] * (V+1)
result = []

for i in range(E):
    num1, num2 = edge[i*2], edge[i*2+1]
    adj_matrix[num1][num2] = 1
    adj_matrix[num2][num1] = 1

dfs(1)

print(f'#{1} {"-".join(map(str, result))}')