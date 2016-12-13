def find_sum(n):
    numbers = []
    i = 1
    ost = n
    while ost > 0:
        if ost == i:
            numbers.append(i)
            ost -= i
        elif ost - i >= i + 1:
            numbers.append(i)
            ost -= i
            i += 1
        else:
            i += 1
    return(numbers)


n = int(input())
r = find_sum(n)
print(str(len(r)))
print(*r, sep=' ')
