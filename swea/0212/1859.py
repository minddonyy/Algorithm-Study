import sys
sys.stdin = open('input_1859.txt', 'r')

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    price = [] * N
    input_data = input()

    tmp = ''
    for c in input_data:
        if c == ' ':
            price.append(int(tmp))
            tmp = ''
        else:
            tmp += c
    if tmp:
        price.append(int(tmp))

    result = 0
    max_sell = 0

    for i in range(N-1, -1, -1):
        if max_sell < price[i]:
            max_sell = price[i]
        else:
            result += max_sell - price[i]

    print(f"#{tc} {result}")



    # price = list(map(int, input().split()))
    # current_word = ""
    # for num in input().split():
    #     price.append(int(num))

    #
    # for _ in range(N):
    #     price.append((int()))










