T = int(input())
for tc in range(1, T+1):
    score = list(map(str, input().strip()))
    score_sum = 0
    total = 0

    for i in range(len(score)):
        if score[i] == 'O':
            score_sum +=1
            total += score_sum
        else:
            score_sum = 0
    print(total)
