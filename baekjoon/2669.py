import sys
sys.stdin = open('input_2669.txt', 'r')
########################################


white = [[0] * 100 for _ in range(100)]



T = 4
count = 0
for tc in range(1, T+1):
    x1, y1, x2, y2 = map(int, (input().split()))
    for i in range(x1,x2):
        for j in range(y1, y2):
            if white[i][j] == 0:
                white[i][j] += 1
                count+=1

print(count)