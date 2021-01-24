import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

# get input and decode it
def inp():
    return input().decode()

# sys.stdout.write() for faster output
def sswrite(val):
    sys.stdout.write(str(val) + '\n')

def intmap():
    return map(int, inp().split(' '))


##################### - solution - #####################

t = int(inp())
def solve(d):
    r = {'N':0, 'S':0, 'W':0, 'E':0}
    
    c=1
    last = []
    for i in range(len(d)):
        if d[i] in 'NWSE':
            r[d[i]] += c
        elif d[i].isdigit():
            c*=int(d[i])
            last.append(d[i])
        elif d[i] == ')':
            c = c//int(last.pop())
    
    a = r['E'] - r['W']
    b = r['S'] - r['N']        
    return int((a%10**9)+1), int((b%10**9)+1)
    
for i in range(1, t+1):
    d = inp()
    a, b = solve(d)
    sswrite('Case #{}: {} {}'.format(i, a, b))
