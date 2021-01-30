t = int(input())
 
 
for i in range(t):
    input()
    l = input()
    z, o = l.count('0'), l.count('1')
    if z == o: print('E')
    elif z > o:
        t = (z-o)%4
        if not t: print('E')
        elif t == 1: print('S')
        elif t == 2: print('W')
        elif t == 3: print('N')
    
    else:
        t = (o-z)%4
        if not t: print('E')
        elif t== 1: print('N')
        elif t == 2: print('W')
        elif t == 3: print('S')
