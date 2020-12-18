t = int(input())


def solve(n):
    if int(n) % 10==0:
        print(1)
        return n

    res = []

    c=0
    for i in range(len(n)):
        if n[i] != '0':
            c+=1
            res.append(n[i]+('0'*(len(n)-i-1)))
    print(c)
    return ' '.join(res)

for i in range(t):
    n = input()
    print(solve(n))
