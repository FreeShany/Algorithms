import random

def read_data():
    s_list = input().split()
    n_intervals = int(s_list[0])
    n_dots = int(s_list[1])
    intervals = []
    for i in range(n_intervals):
        s = input().split()
        intervals.append((int(s[0]), int(s[1])))
    dots = [int(n) for n in input().split()]
    return intervals, dots


def merge_dots_and_intervals(dots, intervals):
    M = []
    i = 0
    for dot in dots:
        M.append((dot, 1, i))
        i += 1
    for interval in intervals:
        M.append((interval[0], 0, 0))
        M.append((interval[1], 2, 0))
    return M


def partition(A, l, r):
    random_i = random.randrange(l, r)
    A[l], A[random_i] = A[random_i], A[l]
    x = A[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        #print("i = %d, j = %d, k = %d" % (i, j, k))
        #print(A[l : r + 1])
        if A[i] < x:
            j += 1
            k += 1
            A[j], A[i] = A[i], A[j]
            if j != k:
                A[i], A[k] = A[k], A[i]
        elif A[i] == x:
            k += 1
            A[i], A[k] = A[k], A[i]

    A[l], A[j] = A[j], A[l]
    return j, k


def quick_sort(A, l, r):
    while l < r:
        m, c = partition(A, l, r)
        quick_sort(A, l, m - 1)
        l = c + 1
    return A

def count_intervals_per_dot(M):
    n = 0
    res = []
    for m in M:
        if m[1] == 0:
            n += 1
        elif m[1] == 2:
            n -= 1
        else:
            res.append([m[0], m[2], n])
    return res


def solve(intervals, dots):
    random.seed(999)
    M = merge_dots_and_intervals(dots, intervals)
    M = quick_sort(M, 0, len(M) - 1)
    n_dots = count_intervals_per_dot(M)
    n_dots = sorted(n_dots, key = lambda n_dots: n_dots[1])
    res = []
    for n_dot in n_dots:
        res.append(n_dot[2])
    return res


def solve_simple(intervals, dots):
    res = []
    for d in dots:
        r = 0
        for interval in intervals:
            if d >= interval[0] and d <= interval[1]:
                r += 1
        res.append(r)
    return res


def generate():
    intervals = []
    dots = []

    for i in range(30):
        l = random.randint(0, 50)
        r = random.randint(0, 50)
        if l > r:
            l, r = r, l
        intervals.append((l, r))

    for i in range(30):
        dots.append(random.randint(0, 50))

    return intervals, dots


def stress_test():
    for i in range(100000):
        intervals, dots = generate()
        res = solve(intervals, dots)
        res_simple = solve_simple(intervals, dots)
        if res != res_simple:
            print("Error!!!!")
            print("Intervals and dots:")
            print(intervals, dots)
            print("Result:")
            print(res)
            print("Result simple:")
            print(res_simple)
            break
        else:
            print("Good! %d" % i)

def main():
    intervals, dots = read_data()
    res = solve(intervals, dots)
    for r in res:
        print(r, end = ' ')
    print('\n')

main()
#stress_test()
