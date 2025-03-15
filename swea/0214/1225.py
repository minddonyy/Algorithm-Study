import sys
from collections import deque
sys.stdin = open('input_1225.txt', 'r')
"""
n 개의 숫자 입력
첫 번째 숫자를 1감소 맨 뒤로
다음 첫번째는 2 감수 다음은 3, 4, 5 ..
숫자가 감소할 때 0보다 작아지면 0이다
그럼 n 자리의 숫자가 암호가 됨

첫번째 숫자 가져와서 i :1부터 ++ 시켜주면서 빼주면 된다
그리고 다시 추가 
반복하면됨
* 5까지만 해야 하는데 계속 함.. 아
"""
########################################
T = 10     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    n = int(input())
    print(f"#{n}", end=" ")
    arr = list(map(int, input().split()))
    i = 0

    while arr[-1] > 0:
        num = arr.pop(0)
        i += 1
        arr.append(num-i)

        if i == 5:
            i = 0

    arr[-1] = 0
    print(*arr)





