def read_data():
    nums = [int(n) for n in input().split()]
    del(nums[0])
    keys = [int(n) for n in input().split()]
    del(keys[0])
    return nums, keys


def find_index(nums, key):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == key:
            return(m + 1)
        elif nums[m] < key:
            l = m + 1
        elif nums[m] > key:
            r = m - 1
    return(-1)



nums, keys = read_data()
res = []
for key in keys:
    res.append(find_index(nums, key))
for r in res:
    print(r, end = ' ')
