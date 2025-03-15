import sys
sys.stdin = open('input_5099.txt', 'r')
from collections import deque
########################################
"""
N개의 피자를 동시에 구울 수 있음
1번부터 M번까지 M개의 피자를 순서대로 넣는다
치즈의 양에 따라 녹는 시간이 달라서 꺼내는 순서를 달라질 수 있음
결과는 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내기

피자는 1번에서만 넣거나 뺄 수 있음
M개의 피자, 처음 뿌려진 치즈의 양이 주어짐, 화덕을 한바퀴 돌 때 녹지 않은 치즈의 양은 반으로 줄어든다
치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그자리에서 남은 피자를 순서대로 넣는다


화덕의 크기만큼 돌았을 때 
피자마다 치즈의 양을 //2 하면 됨
화덕의 크기가 3이면 3만큼 돌고 /2 하고 0이 안 된 애들은 그대로 돌고 
아닌 애들은 pop 하고 뒤에 애들 넣으면 됨

1 2 3 4 5
7 2 6 5 3
"""

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : 화덕의 크기 M : 피자 개수
    cheese = list(map(int,input().split())) # M개만큼 치즈의 양을 줌

    queue = deque()
    last_pizza = None # 마지막 피자
    count = 0

    for i in range(N):
        queue.append((i + 1, cheese[i])) # 큐에 피자인덱스, 치즈 넣기

    while len(queue)>0:
        pizza, p_cheese = queue.popleft() # 첫번째에서 피자 빼고
        p_cheese //= 2 # 치즈 /2

        if p_cheese > 0:
            queue.appendleft((pizza, p_cheese))
        else:
            last_pizza = pizza # 계속 돌았는데 치즈가 0보다 계속 크다면 그게 마지막 피자

    print(last_pizza)


