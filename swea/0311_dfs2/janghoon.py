import sys
sys.stdin = open("input.txt", "r")
"""
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 두 정수 N, B(1 ≤ N ≤ 20, 1 ≤ B ≤ S)가 공백으로 구분되어 주어진다.

S는 두 번째 줄에서 주어지는 점원들 키의 합이다.

두 번째 줄에는 N개의 정수가 공백으로 구분되어 주어지며, 각 정수는 각 점원의 키 Hi (1 ≤ Hi ≤ 10,000)을 나타낸다.
"""
def dfs(idx, h_sum):
    global max_height

    if h_sum >= max_height:
        return

    if N == idx:
        if h_sum >= B:
            max_height = min(max_height, h_sum)
        return

    dfs(idx+1, h_sum+heights[idx])
    dfs(idx+1, h_sum)

T= int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    max_height = float("inf")

    dfs(0, 0)

    print(f"#{tc}",max_height-B)


