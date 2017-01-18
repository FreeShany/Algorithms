def read_data():
    a = []
    n = int(input())
    s_list = input().split()
    for s in s_list:
        a.append(int(s))
    return a

def merge(a1, a2):
    i = 0
    sub_m = []
    sub_degree = 0
    while len(a1) > 0 and len(a2) > 0:
        if a1[0] <= a2[0]:
            sub_m.append(a1[0])
            sub_degree += i
            del(a1[0])
        else:
            sub_m.append(a2[0])
            i += 1
            del(a2[0])
    if len(a1) > 0:
        sub_degree += i * len(a1)
        sub_m += a1
    else:
        sub_m += a2
    return sub_m, sub_degree

def count_entrapy_degree(a_draft):
    degree = 0
    if len(a_draft) > 1:
        i = len(a_draft)
        m = []
        while i >= 2:
            sub_m, sub_degree = merge(a_draft[len(a_draft) - i], a_draft[len(a_draft) - i + 1])
            degree += sub_degree
            m.append(sub_m)
            i -= 2
        if i == 1:
            m.append(a_draft[-1])
        degree += count_entrapy_degree(m)
        return degree
    if len(a_draft) == 1:
        return 0

a_original = read_data()
a_draft = []
for n in a_original:
    a_draft.append([n])
print(count_entrapy_degree(a_draft))
