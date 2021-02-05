n = int(input())
d = list(map(int, input().split()))
a, b = 0, len(d)
l=[]
s1=s2=0
while a<b:
    while s1>s2 and a<b:
        b-=1
        s2+=d[b]
    while s2>s1 and a<b:
        s1+=d[a]
        a+=1
    if s1==s2:
        l.append(s1)
        b-=1
        s2+=d[b]

print(l[-1])
