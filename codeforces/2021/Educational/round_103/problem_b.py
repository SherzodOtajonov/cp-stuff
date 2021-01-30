t = int(input())
 
def solve(n, k):
    l = list(map(int, input().split()))
    c=l[0]
    r=0
    for i in range(1, len(l)):
        cur = int((100*l[i]+k-1)/k)
        r = max(r, cur-c)
        c+=l[i]

    return r

for i in range(t):
    n, k = map(int, input().split())
    print(solve(n,k))
