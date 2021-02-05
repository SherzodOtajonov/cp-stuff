n = int(input())
d={}
for i in range(n):
    c = input()
    if c in d:
        d[c]+=1
        print(f'{c}{d[c]}')
    else:
        print('OK')
        d[c]=0
