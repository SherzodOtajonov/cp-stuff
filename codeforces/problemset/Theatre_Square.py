n, m, a = [int(i) for i in input().split(' ')]
from math import ceil

def solve(n, m, a):
    return ceil(n/a) * ceil(m/a)
print(solve(n, m, a))
