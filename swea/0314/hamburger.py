import sys
sys.stdin = open("input_ham.txt")
"""
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 재료의 수, 제한 칼로리를 나타내는 N, L
(1 ≤ N ≤ 20, 1 ≤ L ≤ 104)가 공백으로 구분되어 주어진다.
다음 N개의 줄에는 재료에 대한 민기의 맛에 대한 점수와 칼로리를 나타내는 Ti, Ki
(1 ≤ Ti ≤ 103, 1 ≤ Ki ≤ 103)가 공백으로 구분되어 주어진다.

민기가 좋아하는 햄버거를 먹으면서도 다이어트에 성공할 수 있도록 정해진 칼로리 이하의 조합 중에서 
민기가 가장 선호하는 햄버거를 조합해주는 프로그램을 만들어보자.

(단 여러 재료를 조합하였을 햄버거의 선호도는 조합된 재료들의 맛에 대한 점수의 합으로 결정되고, 
같은 재료를 여러 번 사용할 수 없으며, 햄버거의 조합의 제한은 칼로리를 제외하고는 없다.)

"""

def hamboogi(idx = 0, ham_sum= 0, k_sum= 0):
    global max_kcal

    if L < k_sum: # 현재 저장된 값보다 작다면 return
        return

    if idx == N:
        max_kcal = max(max_kcal, ham_sum)
        return

    hamboogi(idx+1, ham_sum+ingredients[idx], k_sum+kcal_list[idx]) # 선택한 경우
    hamboogi(idx+1, ham_sum, k_sum) # 선택하지 않은 경우

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    ingredients = []
    kcal_list = []
    max_kcal = float('-inf')
    for i in range(N):
        a, b = map(int,input().split())
        ingredients.append(a)
        kcal_list.append(b)

    hamboogi()

    print(f"#{tc}", max_kcal)




