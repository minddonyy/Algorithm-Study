import sys
sys.stdin = open('input_2527.txt', 'r')
########################################

T = 4   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
