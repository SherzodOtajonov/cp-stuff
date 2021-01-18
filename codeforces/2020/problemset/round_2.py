t = int(input())


def solve(n, k):
    c = 0
    a = 0
    while c!=k:
        a+=1
        if a%3 !=0:
            c+=1
    return a



for i in range(t):
    n, k = [int(i) for i in input().split()]
    print(solve(n, k))

