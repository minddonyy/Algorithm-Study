import sys
sys.stdin = open('input.txt', 'r')
########################################

def hamboogi(idx, s_sum, k_sum):
    global max_hamboogi

    if L < k_sum: # 제한된 칼로리보다 더한 칼로리가 높다면 가지치기
        return

    if idx == N: # 다 골랐으면
        max_hamboogi = max(s_sum, max_hamboogi) # 가장 높은 햄부기 갱신
        return

    hamboogi(idx+1, s_sum+scores[idx], k_sum+kcalories[idx]) # 선택 o
    hamboogi(idx + 1, s_sum, k_sum) # 선택 x

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N, L = map(int, input().split()) # 재료의 수, 제한 칼로리
    scores = []
    kcalories = []
    max_hamboogi = 0

    for _ in range(N): # 맛 점수랑 칼로리 받아오기
        a, b = map(int, input().split())
        scores.append(a)
        kcalories.append(b)


    hamboogi(0, 0, 0)

    print(f"#{tc}", max_hamboogi)

