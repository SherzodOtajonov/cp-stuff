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


def solve(n):
    l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    res = ['9', '8', '9', '0']
    
    if n < 4:
        return ''.join(res[:n])
    res.pop()
    for i in range(n-3):
        res.append(l[i%len(l)])
    return ''.join(res)

for i in range(t):
    n = int(inp())
    print(solve(n))
