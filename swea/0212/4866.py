import sys
sys.stdin = open('input_4866.txt', 'r')
########################################
def check_matching(data):
    stack = []
    matching_dict = {')': '(', '}': '{'}
    for char in data:
        if char in matching_dict.values():
            stack.append(char)
        elif char in matching_dict.keys():
            if len(stack) == 0:
                return False
            if stack[-1] != matching_dict[char]:
                return False
            stack.pop()

    return not stack

T = int(input())     # Test case 개수를 받아오는 코드

for tc in range(1, T+1):
    test_str = []
    test_str.append(input().strip())
    for ts in test_str:
        print(f"#{tc} {int(check_matching(ts))}")

