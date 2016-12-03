import numpy as np

def matrix_multiply_divided(m1, m2, m):
    r = np.zeros(shape=(2,2))
    r[0][0] = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % m
    r[0][1] = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % m
    r[1][0] = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % m
    r[1][1] = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % m
    return(r)

def matrix_power_binary(p, n, m):
    if n == 1:
        return(p)
    if n % 2 == 0:
        r = matrix_power_binary(p, n // 2, m)
        r = matrix_multiply_divided(r, r, m)
        return(r)
    else:
        r = matrix_power_binary(p, n - 1, m)
        r = matrix_multiply_divided(r, p, m)
        return(r)


s = input().split()
n = int(s[0])
m = int(s[1])
pp = np.array([[1, 1], [1, 0]])
p = matrix_power_binary(pp, n, m)
print(int(p[1][0]))
