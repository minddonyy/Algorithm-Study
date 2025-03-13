import sys
sys.stdin = open("input_5205.txt", "r")

def quick_sort(arr):
    pass

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    unsorted_list = list(map(int, input().split()))

    quick_sort(unsorted_list)
