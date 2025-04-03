import sys
import heapq
sys.stdin = open("input.txt", "r")

def prim(vertices, edges):
    mst = []

    adj_list = {v: [] for v in vertices}
    for start_v, end_v, w in edges:
        adj_list[start_v].append((end_v, w))
        adj_list[end_v].append((start_v, w))

    visited = set()
    init_vertex = vertices[0]
    min_heap = [[w, init_vertex, e] for e,w in adj_list[init_vertex]]
    heapq.heapify(min_heap)
    visited.add(init_vertex)

    while min_heap:
        weight, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited: continue

        visited.add(end_v)
        mst.append((start_v, end_v, weight))

        for adj_v, adj_w in adj_list[end_v]:
            if adj_v in visited: continue
            heapq.heappush(min_heap, [end_v, adj_v])

    return mst

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_points = list(map(int, input().split()))
    y_points = list(map(int, input().split()))
    e = float(input())




