def pack_optimally(goods, capacity):
    space = capacity
    cost = 0
    for good in goods:
        if space > good[1]:
            cost += good[0]
            space -= good[1]
        else:
            cost += good[0] * (space / good[1])
            return(cost)
    return(cost)

s = input().split()
n = int(s[0])
w = int(s[1])
goods = []
for i in range(n):
    s = input().split()
    goods.append((int(s[0]),int(s[1])))
goods = sorted(goods, key = lambda g: g[0] / g[1], reverse = True)
print("{:.3f}".format(pack_optimally(goods, w)))
