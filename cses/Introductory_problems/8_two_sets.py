n = int(input())
t = int(n*(n+1)/2)

if (t%2): print("NO")
else:
    sa = sb = 0
    a, b = [], []
    for i in range(n, 0, -1):
        if sa+i<=t/2:
            sa+=i
            a.append(i)
        elif sb+i<=t/2:
            sb+=i
            b.append(i)
    print("YES")
    print(len(a))
    print(*sorted(a))
    print(len(b))
    print(*sorted(b))
