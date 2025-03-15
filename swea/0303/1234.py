import sys
sys.stdin = open("input_1234.txt", "r")

T = 10
for tc in range(1, T+1):
    N, password = input().split()
    N = int(N)
    stack = []

    for digit in password:
        if stack and stack[-1] == digit:
            stack.pop()
        else:
            stack.append(digit)

    result = "".join(stack)
    print(f"#{tc} {result}")

