import io, os, sys
from math import sqrt
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
# get input and decode it
def inp():
    return input().decode()
 
# sys.stdout.write() is a faster version of print()
def sswrite(val):
    sys.stdout.write(str(val) + '\n')
 
def intmap():
    return map(int, inp().split(' '))
 
t = int(inp())
 
def solve(n, d):
    l = list(intmap())
    l.sort()
    if l[-1] > d:
        return l[0] + l[1] <= d
    return True
 
for i in range(t):
    n, d = intmap()
    if (solve(n, d)):
        print('YES')
    else:
        print('NO')
    
