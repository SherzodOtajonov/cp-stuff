t = int(input())

for i in range(t):
    n = int(input())
    if n < 2020: print('NO')
    else:
        f=0
        j=0
        while j<=n:
            if (n-j)%2021==0:
                print('YES')
                f=1
                break
            j+=2020
        if not f: print('NO')
