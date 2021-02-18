t = int(input())
 
for i in range(t):
    n, k = map(int, input().split())
    k-=1
    if n%2==0: print(k%n+1)
    else:
        a=n//2
        t=k//a
        k-=t
        k+=2*t
        print(k%n+1)
