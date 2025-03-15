import sys
sys.stdin = open("input_1213.txt", "r")

T = 10
for tc in range(1, T+1):
    N = int(input())
    find_string = str(input())
    origin_string = str(input().strip())

    count = 0
    for i in range(len(origin_string) - len(find_string) +1):
        if origin_string[i:i + len(find_string)] == find_string:
            count+=1

    print(f"#{N}", count)
