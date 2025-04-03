import sys
sys.stdin = open("input.txt", "r")

class DisjointSet:
    def __init__(self, v):
        self.p = [0] * (v + 1)

    def make_set(self, x):
        self.p[x] = x

    def find_set(self,x):
        if x!= self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]


    def union(self, x, y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px < py:
            self.p[py] = px
        else:
            self.p[px] = py


def mst_kruskal(edges):
    mst = []
    w_sum = 0
    ds = DisjointSet(V)

    for i in range(V + 1):
        ds.make_set(i)

    edges.sort(key=lambda x:x[2])
    #정렬된 간선
    #가장 작은 값
    for edge in edges:
        s,e,w = edge
        if ds.find_set(s) != ds.find_set(e):
            ds.union(s, e) # 같은 그룹이 아니라면 연결을 해야 함
            mst.append(edge)
            w_sum += w

    return w_sum


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    result = mst_kruskal(edges)

    print(f"#{tc}", result)