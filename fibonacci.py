def fibonachi(n):
    fib_n = [0, 1]
    for _ in range(2, n + 1):
        fib_n[0], fib_n[1] = fib_n[1], fib_n[0] + fib_n[1]
    return fib_n[1]


n = input("Type a real number from 1 to 40: ")
fib_n = fibonachi(n)
print "Answer for n = %d is %d" % (n, fib_n)
