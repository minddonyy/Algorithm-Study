import sys
sys.stdin = open('input_9367.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    C = list(map(int,input().split()))

    count = 1
    result = 1
    for i in range(len(C)-1):
        if C[i] < C[i+1]: # 지금값이랑 다음값이랑 비교
            count+=1 # 카운트 1
            result = max(count, result) #카운트한 값중에 제일 큰 거
        else:
            count=1

    print(f"#{tc} {result}")


