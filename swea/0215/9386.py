import sys
sys.stdin = open('input_9386.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input()))
    result = 0
    count = 0
    for i in arr:
        if i == 1:
            count+=1
            if count > result:
                result = count
        else:
            count = 0

    print(f"#{tc} {result}")