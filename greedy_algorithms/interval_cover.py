def interval_cover(l, n):
    i = 1
    r = []
    while i <= n:
        dot = l[i-1][1]
        r.append(dot)
        while i <= n and dot >= l[i-1][0] and dot <= l[i-1][1]:
            i += 1
    return(r)

n = int(input())
intervals = []
for i in range(n):
    s = input().split()
    intervals.append((int(s[0]),int(s[1])))
intervals = sorted(intervals, key=lambda interval: interval[1])
r = interval_cover(intervals, n)
print(str(len(r)))
print(*r, sep=' ')
