def bubble_sort(arr):
    length = len(arr)

    for i in range(length):
        for j in range(i - length - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr1 = [1,9,4,2]
print(bubble_sort(arr1))
