n = int(input())
a = input().split()
d = {'4':0, '8':0, '15':0, '16':0, '23':0, '42':0}
l = ['4', '8', '15', '16', '23', '42']
 
for i in a:
    if i in l:
        if i=='4': d[i]+=1
        else:
            if d[l[l.index(i)-1]]>d[i]: d[i]+=1
 
print(len(a)-min(d.values())*6)
