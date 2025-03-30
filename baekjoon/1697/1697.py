"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.


1. 수빈이랑 동생이 있는 위치의 1차원 배열을 만든다 [ 1, 0, 0 , 1] 이런식
2. 그리고 queue에 있는 위치를 넣어줌
3. while queue를 하면서 x-1 , x+1, 2 * x 를 델타탐색처럼 해줌
4. nx 를 append 해준다
5. while내에서 if x가 k의 값이 같다면 가장 작은 time을 리턴한다
"""
from collections import deque
def find():
    queue = deque()
    queue.append(N)
    while queue:
        subin = queue.popleft()

        if subin == K:
            return visited[subin]

        for next in (subin-1, subin+1, 2*subin):
            if 0<= next < (max_n+1) and not visited[next]:
                visited[next] = visited[subin]+1
                queue.append(next)

    return -1

max_n = 100000
N, K = map(int, input().split())
visited = [0] * (max_n+1)

print(find())





