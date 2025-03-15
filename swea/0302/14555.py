import sys
sys.stdin = open("input_14555.txt", "r")

T = int(input())
for tc in range(1, T+1):
    st = str(input())
    count = 0
    for i in range(len(st) - 1):
        if st[i] == '(' and st[i + 1] == ')':
            count+=1
        elif st[i] == '(' and st[i + 1] == '|':
            count+=1
        elif st[i] == '|' and st[i + 1] == ')':
            count+=1

    print(f"#{tc}", count)