from collections import Counter
n,k = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(a, reverse=True)
s = sum(b[:k])
print(s)
c = Counter(b[:k])
l=[]
i=j=x=0
while len(l)<k-1 and i<len(a):
    if a[i] in c and c[a[i]]>0:
        c[a[i]]-=1
        j+=1
        l.append(i+1-x)
        x=i+1
    i+=1
l.append(len(a)-x)
print(*l)
