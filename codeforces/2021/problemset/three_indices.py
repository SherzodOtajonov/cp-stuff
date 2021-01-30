t = int(input())

for i in range(t):
    input()
    p = list(map(int, input().split()))
    c, r = 0, 1
    l = []
    for i in range(1, len(p)):
        if not c and p[i-1] - p[i]<0:
            c=1
            l.append(i)
        elif c and p[i-1] - p[i]>0:
            l.extend([i, i+1])
            print('YES')
            print(*l)
            r=0
            break
    if r: print('NO')
