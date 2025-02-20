import sys
sys.stdin = open('input_5205.txt', 'r')
########################################

T = int(input())     # Test case 개수를 받아오는 코드
for tc in range(1, T+1):
    N = int(input())
    # 타임테이블 끝나는 시간으로 정렬
    time_table = sorted(list(tuple(map(int, input().split())) for _ in range(N)), key=lambda x:x[1])

    count, before = 0, 0
    for start, end in time_table:
        if before <= start:
            count+=1
            before = end

    print(f"#{tc} {count}")
