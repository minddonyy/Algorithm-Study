import sys
sys.stdin = open("input.txt", "r")
### 9시 17분 시작
"""
N개의 재료, 신맛 S 쓴맛 B
여러 재료를 이용해서 요리할 때, 그 음식의 신맛은 사용한 재료의 신맛의 곱이고, 쓴맛은 합이다.

신맛과 쓴맛의 차이가 가장 작은 요리를 만드는 프로그램을 작성하시오. 

1
3 10
"""

def doyoung(idx, s_gob, b_hap, cnt):
    global min_result

    min_data = abs(s_gob - b_hap)

    if idx == N:
        if min_data < min_result and cnt > 0:
            min_result = min(min_result, min_data)
        return

    doyoung(idx+1, s_gob*s_list[idx], b_hap+b_list[idx], cnt+1)
    doyoung(idx+1, s_gob, b_hap,cnt)


N = int(input())
s_list = []
b_list = []
min_result = float("inf")

for _ in range(N):
    s,b = map(int, input().split())
    s_list.append(s)
    b_list.append(b)


doyoung(0, 1, 0, 0) # 곱이니까 1로 줘야함 0을 곱하면 0이 됨

print(min_result)


