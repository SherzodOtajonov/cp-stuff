t = int(input())

for i in range(t):
    n = int(input())
    while n%2==0:
        n/=2
    if n==1:
        print('NO')
    else: print('YES')
