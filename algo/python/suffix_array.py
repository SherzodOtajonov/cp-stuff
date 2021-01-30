# implement suffix array

s = input()
s += '$'
n = len(s)
c = [0 for _ in range(n)]

a = [[s[i], i] for i in range(n)]
a.sort()

p = [a[i][1] for i in range(n)]

c[p[0]] = 0
for i in range(1, n):
    if a[i][0] == a[i-1][0]: c[p[i]] = c[p[i-1]]
    else: c[p[i]] = c[p[i]] = c[p[i-1]]+1

k = 0
while (1<<k < n):
    # k -> k+1
    a = [0 for _ in range(n)]
    for i in range(n):
        a[i] = [[c[i], c[(i+(1<<k))%n]], i]
    a.sort()

    for i in range(n): p[i] = a[i][1]
    c[p[0]] = 0
    for i in range(1, n):
        if a[i][0] == a[i-1][0]: c[p[i]] = c[p[i-1]]
        else: c[p[i]] = c[p[i-1]]+1
    k+=1
for i in range(n): print(p[i], end=' ')
