import sys
sys.stdin = open('input_18124.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):

    arr = list(map(int, input().split()))
    N = len(arr)
    max_arr = 2 ** N #생성가능한총개수
    result = 0 #결과값

    set_list = []
    for i in range(max_arr):
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(arr[j])
        set_list.append(subset)

    for sl in set_list:
        if sum(sl) == 0 and len(sl)!=0: # 0인걸 찾아야 하는데 길이가 0 이상인 것도 찾아야 함
            result = 1

    print(f"#{tc} {result}")

