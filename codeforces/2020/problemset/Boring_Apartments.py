t = int(input())

def solve(x):
    d = {1:9, 2:7, 3:4, 4:0}
    fst = str(x)[0]
    l = len(str(x))
    mx = 10*int(fst)
    return mx - d[l]

for i in range(t):
    x = int(input())
    print(solve(x))
