t = int(input())

def solve(n, x):
    from math import ceil
    if n < 3: return 1
    return ceil((n-2)/x)+1

for i in range(t):
    n, x = [int(j) for j in input().split(' ')]
    print(solve(n, x))
