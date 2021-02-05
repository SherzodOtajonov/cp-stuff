n = int(input())
d = list(map(int, input().split()))
d.sort()
a = d[-1]
x, y=[], []
for i in range(n):
    if a%d[i]==0 and d[i] not in x: x.append(d[i])
    else: y.append(d[i])

print(a, max(y))
