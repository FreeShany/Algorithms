def packing(l, w):
    space = w
    r = 0
    for good in l:
        if space > good[1]:
            r = round(r + good[0], 3)
            space -= good[1]
        else:
            r = round(r + good[0] * (space / good[1]), 3)
            return(r)
    return(r)

s = input().split()
n = int(s[0])
w = int(s[1])
goods = []
for i in range(n):
    s = input().split()
    goods.append((int(s[0]),int(s[1])))
goods = sorted(goods, key = lambda g: g[0] / g[1], reverse = True)
print("{:.3f}".format(packing(goods, w)))
