import sys
sys.stdin = open('input_22375.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    a,b = map(int,input().split())

    print(a,b)