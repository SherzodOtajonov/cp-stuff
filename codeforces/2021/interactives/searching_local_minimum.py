from sys import stdout as sd 
 
def solve():
    n = int(input())
    l, u = 0, n
    print("?", 1)
    sd.flush()
    a = int(input())
    if a==1: return '! 1'
 
    print("?", 2)
    sd.flush()
    x = int(input())
 
    print("?", n)
    sd.flush()
    b = int(input())
    if b==1: return f'! {n}'
    
    print("?", n-1)
    sd.flush()
    y = int(input())
    
 
    if a<x:
        return '! 1' 
    elif b<y:
        return f'! {n}'
        
    while True:
        m = (l+u)//2
 
        print('?', m)
        sd.flush()
        c=int(input())
        if c==1:
            return f'! {m}'
            
        print('?', m-1)
        sd.flush()
        lm = int(input())
 
        if lm==1:
            return f'! {m-1}'
 
        print('?', m+1)
        sd.flush()
        mr = int(input())
 
        if mr==1:
            return f'! {m+1}'
 
        if lm>c and c<mr:
            return f'! {m}'
            break
        elif lm<c: u=m-1
        elif mr<c: l=m+1
 
 
print(solve())
