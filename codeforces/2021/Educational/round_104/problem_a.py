t = int(input())
 
for i in range(t):
    n = int(input())
    l =list(map(int, input().split()))
    m = min(l)
    print(n-l.count(m))
