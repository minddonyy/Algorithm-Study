import sys
sys.stdin = open("input_1231.txt", "r")

def inorder(value):
    if value <= N:
        inorder(value * 2)
        print(data[value], end="")
        inorder(value * 2 + 1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [0] * (N+1)

    for i in range(N):
        arr = list(input().split())
        data[i+1] = arr[1]

    print(data)
    print(f"#{tc}", end=" ")
    inorder(1)
    print()