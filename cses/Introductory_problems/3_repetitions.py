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


s = inp()

def solve(s):
    ml=0
    c=0
    for i in range(len(s)-1):
        if s[i] != s[i+1] or i+2==len(s):
            ml = max(ml, c+1)
            c=0
        else:
            c+=1
    return ml
print(solve(s))
