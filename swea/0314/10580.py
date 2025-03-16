import sys
sys.stdin = open("input_10580.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = 0
    lines = []
    for i in range(N):
        start, end = map(int, input().split())
        lines.append((start, end))

        if lines:
            for start_2, end_2 in lines:
                if (start < start_2 and end > end_2) or (start > start_2 and end < end_2):
                    count += 1
        # lines.append((start,end))
        #
        # for s1, e1 in lines:
        #     for s2, e2 in lines:
        #         if s1 < s2 and e1 > e2:
        #             count += 1
        #         elif s1 > s2 and e1 < e2:
        #             count += 1


    print(f"#{tc}", count)










