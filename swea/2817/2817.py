import sys
sys.stdin = open('input.txt', 'r')
########################################

def calc_sum(idx, n_sum):
    global result

    if n_sum > K: # 더한 값이 K보다 크다면 가지치기
        return

    if idx == N: #다 선택했으면
        if n_sum == K: # K 랑 더한 값이 같아야 하니까 조건 추가하고
            result += 1 # 경우의 수를 찾아야 하니까 +1씩 추가
        return

    calc_sum(idx + 1, n_sum + numbers[idx]) #선택했을때
    calc_sum(idx + 1, n_sum) #선택하지 않았을 때

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    result = 0

    calc_sum(0, 0)

    print(f"#{tc}",result)