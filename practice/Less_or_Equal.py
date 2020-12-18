n, k = [int(i) for i in input().split(' ')]

def solve(n, k):
    if k>n: return '-1'
    s = [int(i) for i in input().split(' ')]
    s.sort()
    try:
        if s[k-1] == s[k]:
            return '-1'
        return s[k-1]+1
    except indexError:
        return s[k]+1
    
        
print(solve(n, k))
