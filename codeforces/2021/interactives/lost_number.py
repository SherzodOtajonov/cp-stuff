from sys import stdout
from math import sqrt
 
sp = [4, 8, 15, 16, 23, 42]
l = []
 
r=int(input('? 1 1\n'))
l.append(int(sqrt(r)))
 
r=int(input('? 2 2\n'))
l.append(int(sqrt(r)))
 
sp.remove(l[0])
sp.remove(l[1])
 
r = int(input('? 3 4\n'))
c=[]
for i in range(len(sp)-1):
    for j in range(i+1, len(sp)):
        if sp[i]*sp[j]==r:
            c += [sp[i],sp[j]]
            sp.remove(c[0])
            sp.remove(c[1])
            break
 
r = int(input('? 4 5\n'))
if c[0]*sp[0]==r:
    l += [c[1],c[0],sp[0],sp[1]]
elif c[1]*sp[0]==r:
    l += [c[0],c[1],sp[0],sp[1]]
elif c[0]*sp[1]==r:
    l += [c[1],c[0],sp[1],sp[0]]
else:  # c[1]*sp[1]==r
    l += [c[0],c[1],sp[1],sp[0]]
 
print('!', *l, '\n')
stdout.flush()
