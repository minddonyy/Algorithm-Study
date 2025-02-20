import sys
sys.stdin = open('input_16546.txt', 'r')
########################################

from itertools import permutations

# 숫자가 1씩 순증하는지 확인
def is_run(target):
    # target의 길이는 3으로 상정 함수를 작성
    # baby gin에서 카드를 판단을 할 때는 무조건 3장을 가지고 판단하기 때문에
    return (target[0] + 1 == target[1]) and (target[1] + 1 == target[2])
    # 단축평가라서 값이 리턴될 것 같지만 사실 비교 연산자여서 값은 T/F

    # if (target[0] + 1 == target[1]) and (target[1] + 1 == target[2])
    #     return True
    # else:
    #     return False

def is_triplet(target):
    # count = 0
    # for card in target:
    #     if target[0] == card:
    #         count += 1
    #
    # return count == 3

    # 세트의 특성 이용
    return len(set(target)) == 1


def is_babygin(target):
    num1 = target[:3]
    num2 = target[3:]

    result1 = is_run(num1) + is_triplet(num1) # 앞 숫자에 대한 런/트리플릿 확인
    result2 = is_run(num2) + is_triplet(num2)

    return (result1 + result2) == 2 # result1, result2 둘 다 런/트리플릿이라면 결과는 2가 나옴


T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    card_list = list(map(int, input().strip()))

    result = 'false'
    for target in permutations(card_list):
        if is_babygin(target):
            result = 'true'
            break

    print(f"#{tc} {result}")