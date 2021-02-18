t = int(input())
for i in range(t):
    l = list(input())
    for j in range(len(l)):
        if j%2:
            if l[j] == 'z': l[j] ='y'
            else: l[j] = 'z'
        else:
            if l[j] != 'a': l[j] = 'a'
            else: l[j] = 'b'
    print(''.join(l))
