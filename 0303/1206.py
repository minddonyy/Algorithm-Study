import sys
sys.stdin = open("input_1206.txt", "r")

T = 10
for tc in range(1, T+1):
    building_count = int(input())
    building_list = list(map(int, input().split()))

    total = 0

    for i in range(2, building_count-2):
        max_height = 0
        for delta in [-2, -1, 1, 2]:
            if 0 <= i + delta <= building_count-1:
                if max_height < building_list[i+delta]:
                    max_height = building_list[i+delta]

        if building_list[i] > max_height:
            total += (building_list[i] - max_height)


    print(total)