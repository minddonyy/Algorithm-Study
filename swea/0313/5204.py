import sys
sys.stdin = open("input_5204.txt", "r")

def merge_sort(arr):
    global cnt
    length = len(arr)
    if length <= 1:
        return arr

    mid = length // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left = merge_sort(left_arr)
    right = merge_sort(right_arr)

    if left[-1] > right[-1]:
        cnt +=1

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # while left and right:
    #     if left[0] < right[0]:
    #         result.append(left.pop(0))
    #     else:
    #         result.append(right.pop(0))
    result.extend(left[i:])
    result.extend(right[j:])

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0

    result = merge_sort(lst)
    print(f"#{tc}", result[N//2], cnt)

