t = int(input())
 
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r=0
    for i in range(n-1):
        mn, mx = sorted([l[i], l[i+1]])
        j=2
        while mn*j<mx:
            mn*=j
            r+=1
    print(r)
