import sys
sys.stdin = open('input_2628.txt', 'r')
########################################
"""
첫줄에는 종이의 가로와 세로의 길이가 차례로 자연수로 주어진다.
 가로와 세로의 길이는 최대 100㎝이다. 둘째 줄에는 칼로 잘라야하는 점선의 개수가 주어진다. 
 셋째 줄부터 마지막 줄까지 한 줄에 점선이 하나씩 아래와 같은 방법으로 입력된다. 
 가로로 자르는 점선은 0과 점선 번호가 차례로 주어지고, 세로로 자르는 점선은 1과 점선 번호가 주어진다. 
 입력되는 두 숫자 사이에는 빈 칸이 하나씩 있다.
 
10 8
3
0 3
1 4
0 2
"""

width, height = map(int, input().split())
cut = int(input())

row_cut = [0, height] #가로를 자름
col_cut = [0, width] # 세로를 자름
result = 0

for _ in range(cut):
    a, b = map(int, input().split())
    if a == 0:
        row_cut.append(b)
    else:
        col_cut.append(b)

row_cut.sort()
col_cut.sort()

for i in range(len(col_cut)-1):
    for j in range(len(row_cut)-1):
        h = col_cut[i + 1] - col_cut[i]
        w = row_cut[j +1] - row_cut[j]

        result = max(result, w*h)

print(result)





