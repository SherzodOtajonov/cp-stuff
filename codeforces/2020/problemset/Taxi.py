n = int(input())
s = [int(i) for i in input().split()]

def solve(n, s):
    from collections import defaultdict
    from math import ceil
    d = defaultdict(lambda : 0)
    for i in s:
        d[i]+=1
    res = d[4]

    while d[1]>0 and d[3]>0:
        res +=1
        d[1]-=1
        d[3]-=1
    twoes = d[2]*2
    if d[1]>0:
        twoes+=d[1]
        
    res += ceil(d[3]*3/4)
    res += ceil(twoes/4)
    return res
print(solve(n, s))
