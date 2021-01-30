n = input()
l=1
f=0
c=0
for i in range(len(n)):
    if n[i] == '1':
        f=1
        c=0
    elif f and n[i] == '4':
        c+=1
    
    if c>2 or (n[i] == '4' and not f) or n[i] not in '14':
        print('NO')
        l=0
        break
if l: print('YES')
