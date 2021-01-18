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


n = int(inp())
x = list(intmap())

def solve(n, x):
    r=0
    m=x[0]
    for i in range(1, n):
        if x[i] < m: r+=m-x[i]
        else: m = x[i]
    return r
print(solve(n, x))
