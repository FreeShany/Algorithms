import math

def sift_up(heap):
    i = heap[0]
    while i > 1 and heap[i] > heap[math.floor(i/2)]:
        heap[math.floor(i/2)], heap[i] = heap[i], heap[math.floor(i/2)]
        i = math.floor(i/2)
    return heap

def sift_down(heap):
    i = 1
    while 2 * i <= heap[0]:
        if (2 * i + 1) <= heap[0]:
            if heap[2 * i + 1] >= heap[2 * i]:
                if heap[i] <  heap[2 * i + 1]:
                    heap[i], heap[2 * i + 1] = heap[2 * i + 1], heap[i]
                    i = 2 * i + 1
                else:
                    return heap
            elif heap[i] < heap[2 * i]:
                heap[i], heap[2 * i] = heap[2 * i], heap[i]
                i = 2 * i
            else:
                return heap
        elif heap[i] < heap[2 * i]:
            heap[i], heap[2 * i] = heap[2 * i], heap[i]
            i = 2 * i
        else:
            return heap
    return heap

def insert(pr, heap):
    if len(heap) >= 2:
        heap[0] += 1
        heap.append(pr)
        heap = sift_up(heap)
    else:
        heap[0] += 1
        heap.append(pr)
    return heap

def extract_max(heap):
    print(heap[1])
    heap[1] = heap[-1]
    del heap[-1]
    heap[0] -= 1
    heap = sift_down(heap)
    return heap

heap = [0]
n = int(input())
for i in range(n):
    s = input().split()
    if len(s) > 1:
        pr = int(s[1])
        command = s[0]
    else:
        command = s[0]
    if command == 'Insert':
        heap = insert(pr, heap)
    if command == 'ExtractMax':
        heap = extract_max(heap)
