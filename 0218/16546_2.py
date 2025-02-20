import sys
sys.stdin = open('input_16546.txt', 'r')
########################################

def is_babygin(count_list):
    # run인지 확인
    # 해당 숫자의 개수가 1이상이면 가능성 있음
    babygin = 0
    i = 0
    while i < 10:
        if count_list[i] >= 3:
            babygin+=1
            count_list[i] -=3
            continue

        #if i <= 7 and count_list[i] >= 1 and count_list[i + 1] >= 1 and if count_list[i + 2] >= 1:
        if i <= 7:
            if count_list[i] >= 1:
                if count_list[i+1] >= 1:
                    if count_list[i+2] >= 1:
                        babygin+=1
                        count_list[i]-=1
                        count_list[i+1]-=1
                        count_list[i+2]-=1
                        continue
        i+=1

    return babygin == 2


    # triplet인지 확인
    # 해당 숫자의 개수가 3이상이면 triplet

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    card_list = list(map(int, input().strip()))

    count_list = [0] * 10

    for i in card_list:
        count_list[i] += 1


    result = 'false'
    if is_babygin(count_list):
        result = 'true'

    print(f"#{tc} {result}")