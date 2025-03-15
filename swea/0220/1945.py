import sys
sys.stdin = open('input_1945.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = [2,3,5,7,11]
    result = [0] * 5 # 결과값 보여줄 리스트

    for i in range(5):
        while N % arr[i] == 0:
            result[i] += 1
            N //= arr[i]

    print(f"#{tc}", *result)