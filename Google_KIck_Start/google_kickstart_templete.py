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


##################### - solution - #####################

t = int(inp())
def solve():
    pass


for i in range(1, t+1):
    sswrite('Case #{}: {}'.format(i, solve()))
