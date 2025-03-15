import sys
sys.stdin = open('input_1217.txt', 'r')
########################################
def power_calc(num, power):
    if power == 0:
        return 1
    return num * power_calc(num, power - 1)

T = 10     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):

    test_num = int(input())
    power_num = list(map(int, input().split()))
    result = power_calc(*power_num)

    print(f"#{test_num} {result}")