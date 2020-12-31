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
 
# instruction of this question was too unclear
 
def solve(n,l):
    evens = odds = e_idx = o_idx = 0
    for i in range(n):
        if l[i] % 2:
            odds += 1
            o_idx += i+1
        else:
            evens += 1
            e_idx += i+1
        if evens >  1 and odds:
            return o_idx
        if odds > 1 and evens:
            return e_idx
 
        
n = int(inp())
l = list(intmap())
sswrite(solve(n, l))
