a = list(map(int, input().split()))
n = a[0]+a[1]+a[2]
an = 1+(n-1)*2
sn = n*(1+an)/2
l=[]
for i in [0, 2, 4]:
    c = 1+(a[i]-1)*2
    m=a[i]*(1+c)/2
    l.append(m)
print(int(sn-sum(l)))


