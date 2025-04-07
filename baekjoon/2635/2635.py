import sys
sys.stdin = open("input.txt", "r")

N = int(input())

result = []

for next in range(1, N+1):
    arr = []
    first_num = N
    second_num = next
    arr = [first_num, second_num]

    temp_num = first_num

    while True:
        third_num = temp_num - second_num

        # if third_num < 0:
        #     break
        #
        # arr.append(third_num)
        # temp_num = second_num
        # second_num = third_num


        if third_num >= 0:
            arr.append(third_num)
            temp_num = second_num
            second_num = third_num
        else:
            break



        if len(result) < len(arr):
            result = []
            result = arr


print(len(result))
print(*result)






