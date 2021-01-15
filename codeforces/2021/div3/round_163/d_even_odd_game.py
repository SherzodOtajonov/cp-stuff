
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
    a.sort(reverse=True)
    even = odd = 0

    for i in range(1, n+1):
        if i%2 and a[i-1] % 2==0:
            even += a[i-1]
        elif i%2==0 and a[i-1]%2:
            odd += a[i-1]
    if even == odd: return 'Tie'
    if even < odd: return 'Bob'
    else: return 'Alice'
for i in range(t):
    n = int(inp())
    a = list(intmap())
    print(solve(n, a))
