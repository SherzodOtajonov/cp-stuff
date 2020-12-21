t = int(input())

def solve(n):
    start = n.index(1)
    cur = 0
    res = 0
    for i in n[start:]:
        if not i:
            cur += 1
        else:
            res += cur
            cur = 0

    return res


for i in range(t):
    input()
    n = [int(j) for j in input().split()]
    print(solve(n))
