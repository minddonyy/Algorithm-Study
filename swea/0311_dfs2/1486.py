import sys
sys.stdin = open("input_1486.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    # 원하는 결과 => B를 넘으면서 최소값
    # 초기값으로는 매우 큰 값을 놔야한다.
    # res = float('INF')
    res = 10000 * N  # 입력값을 계산해서 최대값을 설정

    # idx : 현재 탐색 중인 직원의 인덱스
    # h_sum: 현재까지 선택한 직원들의 키의 합
    def dfs(idx, h_sum):
        global res

        # 키를 누적하고 있는데, 이미 res를 넘어서면 더 진행할 필요가 없다.. .
        # 백트래킹 (가지치기)
        if h_sum >= res:
            return

        if idx == N:  # 모든 직원을 탐색했다.
            if h_sum >= B:  # 직원들의 키의 합이 B를 넘는다.
                # B를 넘는 애들 중에서 최소값
                res = min(res, h_sum)
            return

        # 현재 idx가 가리키는 직원을 포함시킨다.
        # 현재 누적 키에 현재 idx 직원을 포함시키고, 다음 직원으로 넘긴다.
        dfs(idx + 1, h_sum + arr[idx])

        # 곱한 케이스
        # dfs(idx + 1, h_sum * arr[idx])

        # 현재 idx가 가리키는 직원을 포함시키지 않아봐요.
        dfs(idx + 1, h_sum)


    # 부분집합을 구할거에요. (재귀로)
    # 재귀함수를 구현할 때 파라미터
    # 1. 재귀함수를 종료하기 위한 파라미터
    # - 선택하고 있는 점원의 인덱스 ( => 요 인덱스가 N에 도달하면 재귀를 중단)
    # 2. 누적해서 가져가고 싶은 값을 파라미터
    # - 여태까지 선택한 점원들의 키의 합을 가져가고 싶다.
    dfs(0, 0)


    print(f"#{test_case}", res-B)
