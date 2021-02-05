t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if b<9: print(0)
    elif set(str(b)) == set('9'):
        print(len(str(b)) * a)
    else: print((len(str(b))-1)*a)
