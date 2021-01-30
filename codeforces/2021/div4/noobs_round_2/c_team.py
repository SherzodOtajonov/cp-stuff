t = int(input())
 
def solve(n, k, l):
    l.sort(reverse=True)
    r=0
    for i in range(len(l)):
        if l[i] >= k: r+=1
        else: break
    if i != len(l)-1:
        l = l[i:]
        i=0
        b=len(l)-1
        while i<b:
            if l[i] >= k:
                r+=1
                i+=1
            else:
                cur = l[i]
                while cur<k and i<b:
                    cur = l[b]+l[i]
                    b-=1
                if cur>=k: r+=1
                i+=1
    return r
for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    print(solve(n, k, l))
