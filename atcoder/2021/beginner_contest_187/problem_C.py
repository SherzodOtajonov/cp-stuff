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


def solve(n):
    s =set()
    for i in range(n):
        c = inp()
        s.add(c)
        if c[0] == '!':
            if c[1:] in s:
                return c[1:]
        else:
            if '!'+c in s:
                return c
            
    return 'satisfiable'
            
n = int(inp())
print(solve(n))
