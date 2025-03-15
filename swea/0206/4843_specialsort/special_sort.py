import sys
sys.stdin = open('4843_input.txt', 'r')
########################################

'''
리스트에서 가장 큰 값, 작은 값을 찾는다
새로운 리스트에 넣는다
기존 리스트에서는 삭제하고 다시 반복한다
'''
T = int(input())   # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    special_array = []

    for i in range(N):
        if len(arr) > 0:
            max_num = max(arr)
            min_num = min(arr)

            arr.remove(max_num)
            arr.remove(min_num)
            if len(special_array) < 10:
                special_array.append(str(max_num))
                special_array.append(str(min_num))
        special_str = ' '.join(special_array)


    print(f"#{tc} {special_str}")

