def fibonachi(n):
    fib_n = [0, 1]
    for i in range(2, n + 1):
        fib_n[0], fib_n[1] = fib_n[1], fib_n[0] + fib_n[1]
    return fib_n[1]


n = int(input())
print(fibonachi(n))
