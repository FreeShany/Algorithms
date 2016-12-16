def cover_intervals(intervals):
    r = [intervals[0][1]]
    for i in range(1, len(intervals)):
        if r[-1] < intervals[i][0]:
            r.append(intervals[i][1])
    return(r)

def read_data():
    n = int(input())
    intervals = []
    for i in range(n):
        s = input().split()
        intervals.append((int(s[0]),int(s[1])))
    return(sorted(intervals, key=lambda interval: interval[1]))

intervals = read_data()
r = cover_intervals(intervals)
print(str(len(r)))
print(*r, sep=' ')
