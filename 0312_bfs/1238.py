import sys
from collections import deque
sys.stdin = open("input_1238.txt", "r")

def bfs(start, depth):
    global max_depth, max_phone # 글로벌 변수로 선언
    queue = deque()
    queue.append((start,depth))
    while queue: # 큐 있을 때
        start_x, depth = queue.popleft() # 정점, 깊이 추출

        # max 깊이랑 가장 큰 값을 찾아야 함
        if max_depth < depth:
            max_depth = depth
            max_phone = start_x

        if max_depth == depth:
            max_phone = max(max_phone, start_x)

        for i in graph[start_x]: # 그래프 순회하면서
            if called[i] == 0: # 방문하지 않은 곳만
                called[i] = 1 # 방문처리
                queue.append((i, depth+1)) # queue에 넣어줌, 값이랑 depth+1
T = 10
for tc in range(1, T+1):
    length, start = map(int, input().split())
    phone_list = list(map(int, input().split()))
    max_depth = 0
    max_phone = 0

    graph = [[] for _ in range (101)]

    for i in range(length//2): # 그래프 형태로 만들어줌
        num1, num2 = phone_list[2*i], phone_list[2*i+1]
        graph[num1].append(num2)

    called = [0] * 101 #visited 배열

    bfs(start, 0) # 처음 시작점이랑 DEPTH넣어줌 depth 는 0

    print(f"#{tc}", max_phone)