t = int(input())

res = dict()

def fair(n, it):
    for i in set(n):
        if i != '0' and it % int(i) != 0:
            return False
    return True

def solve(n):
    org = n
    it = int(n)

    while True:
        try:
            res[it]
            return res[it]
        except KeyError:
            if fair(str(it), it):
                res[int(org)] = it
                return it
            it += 1
        
for i in range(t):
    n = input()
    print(solve(n))
