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


def solve(n, k, a):
    c=1
    r=0
    for i in range(1, n):
        if a[i-1] -  a[i] == 1:
            c+=1
        else: c=1
        if a[i] == 1  and c>=k:
            r+=1
            c=1
    
    return r

    
for i in range(1, t+1):
    n,k = intmap()
    a = list(intmap())
    sswrite('Case #{}: {}'.format(i, solve(n, k, a)))
