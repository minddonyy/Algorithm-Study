import sys
sys.stdin = open("input.txt", "r")

<<<<<<< HEAD
"""
표준 입력으로 다음 정보가 주어진다. 
첫 번째 줄에는 도시의 개수를 나타내는 정수 N(2 ≤ N ≤ 100,000)이 주어진다. 
다음 줄에는 인접한 두 도시를 연결하는 도로의 길이가 제일 왼쪽 도로부터 N-1개의 자연수로 주어진다.
 다음 줄에는 주유소의 리터당 가격이 제일 왼쪽 도시부터 순서대로 N개의 자연수로 주어진다. 
 제일 왼쪽 도시부터 제일 오른쪽 도시까지의 거리는 1이상 1,000,000,000 이하의 자연수이다. 
 리터당 가격은 1 이상 1,000,000,000 이하의 자연수이다. 
"""

N = int(input())
lines = list(map(int, input().split()))
gas_costs = list(map(int, input().split()))
min_result = 999999999
gas = 0

for i in range(N-1):
    print(gas_costs[i], gas_costs[i+1])
=======
N = int(input()) # 도시의 개수
load = list(map, int(input().split())) # 도시를 잇는 도로의 길이
price = list(map, int(input().split()))

for i in range(N):
    pass
>>>>>>> 3726f8e3032ad8328d62f92ff83a0538296278f2
