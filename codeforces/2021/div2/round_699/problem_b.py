t = int(input())
 
for i in range(t):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    j=0
    while True:
        if (len(h)-2==j and h[j]>=h[j+1]) or j==len(h)-1:
            print(-1)
            break
        if h[j]>=h[j+1]: j+=1
        else:
            h[j]+=1
            k-=1
            if not k:
                print(j+1)
                break
            j=0
