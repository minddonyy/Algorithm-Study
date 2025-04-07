import sys
sys.stdin = open("input.txt", "r")

def garo():
    res = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if visitied[i][j] == 1:
                count +=1
        if count == 5:
            res += 1

    return res

def sero():
    res = 0
    for i in range(N):
        count = 0
        for j in range(N):
            if visitied[j][i] == 1:
                count+=1
        if count == 5:
            res += 1

    return res

def diagonal():
    res = 0
    count = 0

    for i in range(N):
        if visitied[i][N-i-1] == 1:
            count+=1
        if count == 5:
            res += 1

    count = 0

    for i in range(N):
        if visitied[i][i] == 1:
            count+=1
        if count == 5:
            res += 1
    return res

N = 5
bingo_pan = [list(map(int, input().split())) for _ in range(N)]
numbers = [list(map(int, input().split())) for _ in range(N)]
visitied = [[0] * N for _ in range(N)]

result = 0
cnt = 0
is_finished = False
for i in range(N):
    for j in range(N):
        current_num = numbers[i][j]
        cnt += 1

        for x in range(N):
            for y in range(N):
                if bingo_pan[x][y] == current_num:
                    visitied[x][y] = 1

        if cnt >= 12:
            result = garo() + sero() + diagonal()
            if result >= 3:
                print(cnt)
                is_finished = True
                break

    if is_finished:
        break



