import sys
sys.stdin = open("input.txt", "r")










from collections import deque
"""
1 : 상, 하, 좌, 우 
2 : 상, 하
3 : 좌, 우
4 : 상, 우
5 : 하, 우
6 : 하, 좌
7 : 상, 좌
각 테스트 케이스의 첫 줄에는 
지하 터널 지도의 세로 크기 N, 가로 크기 M, 
맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.
"""

dxy = []
def find_place(x, y, cnt = 1):
    queue = deque()
    queue.append((x,y))


    while queue:
        x, y = queue.popleft()

        #cnt 를 반환해야 하는 조건이 필요함

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y

            if under_map[nx][ny] != 0

    pass

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    under_map = [list(map(int, input().split())) for _ in range(N)]

    find_place(R, C)