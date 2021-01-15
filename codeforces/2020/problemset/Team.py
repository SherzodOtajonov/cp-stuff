n = int(input())

def solve(n):
    res = 0
    for i in range(n):
        l = [int(i) for i in input().split(' ')]
        if l.count(1) >=2:
            res +=1
    return res
print(solve(n))
