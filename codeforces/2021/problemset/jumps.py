t = int(input())

def solve(x):
    c, i = 0, 1
    while c<x: 
        c+=i
        i+=1
    if c==x+1: return i
    return i-1

for i in range(t):
    x = int(input()) 
    print(solve(x))
