import sys
sys.stdin = open("input_ham.txt", "r")

def ham(idx, i_sum, k_sum):
    global max_kcal

    if k_sum > L:
        return

    if N == idx:
        max_kcal = max(max_kcal, i_sum)
        return

    ham(idx+1, i_sum + ingredients[idx], k_sum + kcal_list[idx])
    ham(idx+1, i_sum, k_sum)



T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    max_kcal = float("-inf")

    ingredients = []
    kcal_list = []

    for _ in range(N):
        a, b = map(int, input().split())
        ingredients.append(a)
        kcal_list.append(b)

    ham(0, 0, 0)

    print(f"#{tc}",max_kcal)