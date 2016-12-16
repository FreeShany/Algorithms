def find_sum(n):
    numbers = []
    i = 1
    while n > 0:
        if n == i:
            numbers.append(i)
            n -= i
        elif n - i >= i + 1:
            numbers.append(i)
            n -= i
            i += 1
        else:
            i += 1
    return(numbers)


n = int(input())
r = find_sum(n)
print(len(r))
print(*r, sep=' ')
