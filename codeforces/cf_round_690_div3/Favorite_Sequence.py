t = int(input())
 
def solve(n, b):
    from math import ceil
    res = []
 
    idx = 0
    while True:
        if idx <= n - (idx +1):
            res.append(b[idx])
        if idx < n - (idx + 1):
            res.append(b[n-(idx+1)])
            idx += 1
        else: return ' '.join(res)
 
for i in range(t):
    n = int(input())
    b = [j for j in input().split(' ')]
    print(solve(n, b))
