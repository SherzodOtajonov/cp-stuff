n = int(input())
 
l = [0,0,0]
i, j = 3, 4
print(f'? 1 3')
f=int(input())
print(f'? 1 2')
r=int(input())
l[2] = f-r
f=r
 
print(f'? 2 3')
r = int(input())
l[1] = r-l[2]
l[0]=f-l[1]
n-=3
for _ in range(n):
    print(f'? {i} {j}')
    r=int(input())
    l.append(r-l[-1])
    i+=1
    j+=1
print('!', end=' ')
print(*l)
