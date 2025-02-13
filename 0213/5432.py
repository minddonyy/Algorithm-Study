import sys
sys.stdin = open('input_5432.txt', 'r')
########################################
def check_data(data):
    matching_dict = {')':'('}
    stack = []
    for char in data:
        if char in matching_dict.values():
            stack.append(char)

    return stack


T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    data = map(str, input().strip())