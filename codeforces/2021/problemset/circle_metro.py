n, a, x, b, y = map(int, input().split())


while True:
    if a==b:
        print('YES')
        break
    if a==x or b==y:
        print('NO')
        break
    if (a+1)%n: a=(a+1)%n
    else: a=n
    if not b-1: b=n
    else: b-=1

