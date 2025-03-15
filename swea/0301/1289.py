import sys

sys.stdin = open("input_1289.txt", "r")
"""
원재가 컴퓨터를 만지다가 실수를 저지르고 말았다. 메모리가 초기화된 것이다.
다행히 원래 메모리가 무슨 값이었는지 알고 있었던 원재는 바로 원래 값으로 되돌리려고 했으나 메모리 값을 바꿀 때 또 문제가 생겼다.
메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌우는 것이다.
예를 들어 지금 메모리 값이 0100이고, 3번째 bit를 골라 1로 설정하면 0111이 된다.
원래 상태가 주어질 때 초기화 상태 (모든 bit가 0) 에서 원래 상태로 돌아가는데 최소 몇 번이나 고쳐야 하는지 계산해보자.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 메모리의 원래 값이 주어진다.
메모리의 길이는 1이상 50이하이다.

[출력]
각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
초기값(모든bit가 0)에서 원래 값으로 복구하기 위한 최소 수정 횟수를 출력한다.

1. origin memory를 0으로 배열의 len만큼 만든다
2. 기존값이랑 비교하고 같으면 continue
3. 다를 경우 0 일 때는 1로 교체 길이만큼.. 1인 경우 0으로 교체... 
4. 바꿀 때마다 count +1
5. 기존에 memory랑 바꾼 거랑 똑같다면 break 하고 count 값을 출력한다
"""

T = int(input())
for tc in range(1, T+1):
    origin_memory = list(map(int, input()))
    length = len(origin_memory)
    count = 0
    wrong_memory = [0] * length  # 0으로 초기화 된 배열
    for i in range(length):
        if wrong_memory == origin_memory:
            break
        if wrong_memory[i] != origin_memory[i]:
            wrong_memory[i:] = [origin_memory[i]] * (length - i)
            count += 1
        else:
            continue

    print(f"#{tc}", count)
