import sys
from collections import deque
sys.stdin = open('input_5097.txt', 'r')
########################################
"""
    맨 앞에 있는 숫자를 맨 뒤로 보냄 
    이거 M 번 반복함 
    그럼 수열 맨 앞에 있는 숫자를 출력한다
    
    5527 731 31274
"""
T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int,input().split()))
    queue = deque()
    for n in range(N):
        queue.append(numbers[n])

    for i in range(M):
        queue.rotate(-1)

    print(f"#{tc} {queue.popleft()}")




