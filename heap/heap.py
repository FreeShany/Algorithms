def sift_up(heap):
    i = heap[0]
    while i > 1 and heap[i] > heap[i // 2]:
        heap[i // 2], heap[i] = heap[i], heap[i // 2]
        i //= 2

def sift_down(heap):
    i = 1
    while 2 * i <= heap[0]:
        max_child_i = 2 * i
        if 2 * i + 1 <= heap[0] and heap[2 * i + 1] >= heap[2 * i]:
            max_child_i = 2 * i + 1
        if heap[i] < heap[max_child_i]:
            heap[i], heap[max_child_i] = heap[max_child_i], heap[i]
            i = max_child_i
        else:
            return

def insert(pr, heap):
    heap[0] += 1
    heap.append(pr)
    sift_up(heap)

def get_max(heap):
    return heap[1]

def extract_max(heap):
    heap[1] = heap[-1]
    del heap[-1]
    heap[0] -= 1
    sift_down(heap)

heap = [0]
n = int(input())
for i in range(n):
    s = input().split()
    command = s[0]
    if len(s) > 1:
        pr = int(s[1])
    if command == 'Insert':
        insert(pr, heap)
    if command == 'ExtractMax':
        print(get_max(heap))
        extract_max(heap)
