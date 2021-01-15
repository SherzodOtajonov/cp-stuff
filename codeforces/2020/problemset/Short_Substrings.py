t = int(input())

def solve(b):
    res = []
    for i in range(0, len(b)-1, 2):
        res.append(b[i])
    res.append(b[-1])
    return ''.join(res)
        

for i in range(t):
    b = input()
    print(solve(b))
