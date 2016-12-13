def fib_last_digit(n):
    fib_last = [0, 1]
    for i in range(2, n + 1):
        fib_last[0], fib_last[1] = fib_last[1], (fib_last[0] + fib_last[1]) % 10
    return fib_last[1]


n = int(input())
print(fib_last_digit(n))
