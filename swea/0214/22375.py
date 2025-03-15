'''


N 개의 전등 (1 ~ N번)
i번 스위치를 조작하면
  i ~ N번까지의 전등의 켜짐/꺼짐이 반대가 된다.

모든 전등의 현재 상태와
스위치 조작 후 상태가 주어지면
최소 몇 개의 스위치를 조작해야 하는지

규칙
현재 상태 : 0 0 0
조작 후   : 0 1 0

첫 번째 (2번 조작) : 0 1 1
두 번째 (3번 조작) : 0 1 0

T : 테스트 케이스 (첫 줄)  (1 <= T <= 10)
N : 스위치의 갯수 (1~N번)  (1 <= N <= 100)
Ai : 조작전 (N개)
Bi : 최종 모양 (N개)

'''
import sys
sys.stdin = open('input_22375.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    # Ai의 첫 번째 칸과 Bi의 첫 번째 칸을 비교
    #  다르면 해당 위치의 스위치를 변경 해야 함
    #    스위치를 변경하게 되면 해당 위치 부터 N까지의 켜짐 => 꺼짐 / 꺼짐 => 켜짐 변환
    #  중요한 것은 변경하는 횟수
    #  같으면 스위치 변경할 필요 없음
    count = 0
    for idx in range(N):
        if Ai[idx] != Bi[idx]: # Ai[idx] 와 Bi[idx] 같지 않다면
            count += 1  # 스위치 횟수 증가
            for jdx in range(idx, N):
                # 켜짐/꺼짐 스위칭
                if Ai[jdx] == 1:
                    Ai[jdx] = 0
                else:
                    Ai[jdx] = 1

    print(f'#{tc} {count}')