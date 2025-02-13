import sys
sys.stdin = open('input_22167.txt', 'r')
########################################

def reverse_data(data):
    if len(data) != 0: #데이터가 있다면
        return data[-1] + reverse_data(data[0:-1])
    else:
        return data


T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    test_str = list(map(str, input().split()))

    for data in test_str:
        print(f"{reverse_data(data)}")