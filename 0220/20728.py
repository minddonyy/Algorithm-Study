import sys
sys.stdin = open('input_20728.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    candy = list(map(int, input().split()))
    candy.sort()

    result = 0
    for i in range(N-K+1):
        pass



    print(f"#{tc} {result}")