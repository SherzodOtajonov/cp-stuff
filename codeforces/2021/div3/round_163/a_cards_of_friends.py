import io, os, sys
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
 
def solve(w, h, n):
    if n == 1: return 'YES'
    c = 1
    while w%2==0:
        c*=2
        w /= 2
    while h%2==0:
        c*=2
        h /= 2
    if c >= n:
        return 'YES'
    return 'NO'
 
for i in range(t):
    w, h, n = intmap()
    print(solve(w, h, n))
