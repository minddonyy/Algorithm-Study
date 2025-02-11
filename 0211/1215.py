import sys

sys.stdin = open('input_1215.txt', 'r')
########################################
dxy = [(0,-1), (0,1), (-1,0), (1,0)]

T = 10  # Test case 개수를 받아오는 코드
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(8)]
    print(arr)
    length = len(arr)






