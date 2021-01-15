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

def solve(n, a):
    for i in range(n-1, -1, -1):
        if i+a[i] < n:
            a[i] += a[i+a[i]]
    return max(a)


for i in range(t):
    n = int(inp())
    a = list(intmap())
    print(solve(n, a))
