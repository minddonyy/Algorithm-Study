import sys
sys.stdin = open('input_1208.txt', 'r')
########################################
"""
1. 가장 큰 높이를 찾아서 빼고
2. 가장 낮은 높이를 찾아서 더한다
3. 그거 반복
4. 그리고 마지막 가장 높은 곳에서 낮은 곳을 뺀다 끝 .. 
"""

T = 10     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    dump = int(input())

    arr = list(map(int, input().split()))

    for d in range(dump):
        max_height = arr.index(max(arr))
        min_height = arr.index(min(arr))

        arr[max_height] -=1
        arr[min_height] +=1

    print(f"#{tc} {max(arr) - min(arr)}")
