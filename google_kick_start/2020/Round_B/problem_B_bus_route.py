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

def solve(n, d):
    l = list(intmap())
    prev = d
    for i in range(n-1, -1, -1):
        prev = (prev // l[i]) * l[i]
    return prev


for i in range(1, t+1):
    n, d = intmap()
    sswrite('Case #{}: {}'.format(i, solve(n, d)))
