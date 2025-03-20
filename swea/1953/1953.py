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

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우
# 파이프별로 갈 수 있는 조건을 만들어줘야함
can_go = {
    (-1, 0) : [1, 2, 4, 7], #상
    (1, 0) : [1, 2, 5, 6], #하
    (0, -1) : [1, 3, 6, 7], #좌
    (0, 1) : [1, 3, 4, 5] # 우
}

def find_place(x, y):
    queue = deque()
    queue.append((x,y,0)) #큐에 넣어줌
    visited[x][y] = 1 #방문처리
    count = 0

    while queue:
        x, y, cnt = queue.popleft()
        # cnt를 반환해야 하는 조건이 필요함
        # cnt랑 L 이랑 비교해야함

        if cnt <= L:
            break

        for dx, dy in dxy:
            nx = dx + x
            ny = dy + y

            cur_location = under_map[nx][ny]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 1 and cur_location != 0:
                if cur_location in can_go[(dx, dy)]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    under_map = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)] # visited 배열

    result = find_place(R, C)

    print(f"#{tc}", result)