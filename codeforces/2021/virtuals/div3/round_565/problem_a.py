t = int(input())
 
def solve(q):
    r=0
    while q!=1:
        if q<=0:
            return -1
        if q%2==0:
            r+=1
            q=q//2
        elif q%3==0:
            r+=1
            q=q*2//3
        elif q%5==0:
            r+=1
            q=q*4//5
        else:
            return -1
    return r
 
for i in range(t):
    q = int(input())
    print(solve(q))
