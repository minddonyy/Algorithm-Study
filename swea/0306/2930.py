# 1.
import sys

sys.stdin = open("input_2930.txt", "r")


def heappush(heap, item):
    heap.append(item)
    _siftup(heap, len(heap) - 1)


def _siftup(heap, idx):
    parent = (idx - 1) // 2  # 부모노드 idx
    while idx > 0 and heap[idx] > heap[parent]:  # 현재 값이 부모노드보다 크다면 올려보내야 함
        heap[idx], heap[parent] = heap[parent], heap[idx]  # 자식노드를 부모노드랑 교체해준다
        idx = parent
        parent = (idx - 1) // 2  # 부모노드 idx


def heappop(heap):
    if len(heap) == 0:
        return -1
    if len(heap) == 1:
        return heap.pop()

    root = heap[0]
    heap[0] = heap.pop()
    _siftdown(0)
    return root


def _siftdown(idx):
    heap_length = len(heap)
    largest_idx = idx
    left_idx = 2 * idx + 1
    right_idx = 2 * idx + 2

    if left_idx < heap_length and heap[largest_idx] < heap[left_idx]:
        largest_idx = left_idx
    if right_idx < heap_length and heap[largest_idx] < heap[right_idx]:
        largest_idx = right_idx

    if idx != largest_idx:
        heap[idx], heap[largest_idx] = heap[largest_idx], heap[idx]
        _siftdown(largest_idx)


T = int(input())
for tc in range(1, T + 1):

    n = int(input())
    heap = []
    result = []
    for _ in range(n):
        arr = list(map(int, input().split()))

        if arr[0] == 1:
            heappush(heap, arr[1])
        else:
            result.append(str(heappop(heap)))


    print(f"#{tc} {' '.join(result)}")
