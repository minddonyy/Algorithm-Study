import sys
sys.stdin = open('input_1926.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = list(input().split())
    number_list = ""
    for i in range(len(N)):
        pass