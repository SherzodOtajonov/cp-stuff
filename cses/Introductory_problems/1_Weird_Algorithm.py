n = int(input())

res = [str(n)]

while n != 1:
    if n%2:
        n = n*3+1
    else:
        n/=2
    res.append(str(int(n)))
print(' '.join(res))
