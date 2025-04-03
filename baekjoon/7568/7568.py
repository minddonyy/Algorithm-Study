import sys
sys.stdin = open("input.txt", "r")

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    cnt = 1
    for j in range(i+1, N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]: # 다른 것보다 크다면
            cnt += 1

    print(cnt)