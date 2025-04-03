import sys
sys.stdin = open('input.txt')


def make_set(x):
    p[x] = x

def find_set(x):
    if x!= p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    # 각 요소의 부모를 찾는다
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    p = [0] * (N+1)
    rank = [0] * (N+1)

    result = []
    for i in range(1, N + 1):
        make_set(i)

    for _ in range(M):
        n, a, b = map(int, input().split())

        if n == 0: # 합집합
            union(a, b)
        else:
            a_result = find_set(a)
            b_result = find_set(b)

            if a_result == b_result:
                result.append(1)
            else:
                result.append(0)

    print(f"#{tc}", ''.join(map(str, result)))
