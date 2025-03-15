import sys
sys.stdin = open('input_4873.txt', 'r')
########################################

def chk_string(data):
    stack = []
    for char in data:
        if len(stack)> 0 and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return stack

T = int(input())     # Test case 개수를 받아오는 코드

for tc in range(1, T+1):
    test_str = []
    test_str.append(input())

    for ts in test_str:
        print(f"#{tc} {len(chk_string(ts))}")
