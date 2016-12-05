def nod(a, b):
    if a == b:
        return(a)
    if a < b:
        if (b % a == 0):
            return(a)
        else:
            return(nod(a, b % a))
    if a > b:
        if (a % b == 0):
            return(b)
        else:
            return(nod(a % b, b))


s = input().split()
a = int(s[0])
b = int(s[1])
print(nod(a, b))
