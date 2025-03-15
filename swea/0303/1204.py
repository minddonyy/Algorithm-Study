import sys
sys.stdin = open("input_1204.txt", "r")

T = int(input())
for tc in range(1, T+1):
    tase_case = int(input())
    score_list = list(map(int, input().split()))

    counting_score = [0] * 101

    for score in score_list:
        counting_score[score] +=1

    max_count = max(counting_score)
    max_score = 0

    for i in range(100, -1, -1):
        if counting_score[i] == max_count:
            max_score = i
            break

    print(f"#{tase_case}", max_score)
