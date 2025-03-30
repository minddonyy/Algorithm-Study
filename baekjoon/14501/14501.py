import sys
sys.stdin = open("input.txt", "r")

def make_money(idx, money_sum):
    global max_money

    if idx >= N:
        max_money = max(max_money, money_sum)
        return

    if idx + time_list[idx] <= N:
        make_money(idx + time_list[idx], money_sum + pay_list[idx])

    make_money(idx+1, money_sum)

N = int(input())
time_list = []
pay_list = []
for _ in range(N):
    t, p = map(int, input().split())
    time_list.append(t)
    pay_list.append(p)

max_money = 0
make_money(0, 0)
print(max_money)


