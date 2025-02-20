import sys
sys.stdin = open('input_4837.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [i+1 for i in range(N)]
    max_set = 2**N # 만들어질수있는최대집합의수를만든다

    set_list = []
    # 일단 경우의 수 만큼 돈다
    for i in range(max_set):
        temp_set = [] # 부분집합
        for j in range(N): # N 개의 원소만큼 돈다
            if i&(1 << j):
                temp_set.append(arr[j])
        set_list.append(temp_set)

    count = 0

    for sl in set_list:
        set_sum = 0
        for num in sl:
            set_sum+=num

    if set_sum == K:
        count += 1

    print(f"#{tc} {count}")
