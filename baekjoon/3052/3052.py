import sys
sys.stdin = open("input.txt", "r")

result = set()
for _ in range(10):
    n = int(input())
    result.add(n % 42)

print(len(result))
