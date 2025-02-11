import sys
sys.stdin = open('input.txt', 'r')
########################################

#아래, (우,좌)
dxy = [[1,0], [0,1], [0,-1]]
#시작점에서 끝까지 내려가서 "2"에 걸맞는 시작점인지 확인하는 함수
def search_ladder(x, y):
    # 원본을 훼손하지 않기 위해서 복사본을 만들어야 한다
    # 방문 여부를 확인하기 위한 복사본 생성
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1 #초기 시작 위치도 방문 체크

    # x 가 99가 아니면 마지막에 도달하지 않았다
    while x != 99:
        # 3방향으로 델타 탐색 시작
        for dx, dy in dxy:
            nx,ny = x + dx, y+dy
            if 0 <= nx < N and 0<=ny < N and data[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                x, y = nx, ny
    return data[x][y] == 2




T = 1     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = 100
    result = -1
    data = [list(map(int,input().split())) for _ in range(N)]

    for j in range(N):
        if data[0][j] == 1:
            # 사다리 탐색을 시작한다.
            if search_ladder(0,j):
                result = j
                break

    print(f"#{tc} {result}")