import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
# get input and decode it
def inp():
    return input().decode()
 
 
# faster print()
def sswrite(val):
    sys.stdout.write(str(val) + '\n')
 
    
def intmap():
    return map(int, inp().split(' '))
 
 
t = int(inp())
 
def solve(n, a):
    sm = sum(a)
    if sm % 2:
        return 'NO'
    
    if a.count(2) == n and n%2:
        return 'NO'
    return 'YES'
    
    
for i in range(t):
    n = int(inp())
    a = list(intmap())
    print(solve(n, a))
