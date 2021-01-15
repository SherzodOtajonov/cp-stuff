n, k = [int(i) for i in input().split(' ')]


def solve(n, k):
    res = 0
    a = input().split(' ')
    c = int(a[k-1])
    for i in range(n):
        if int(a[i]) >= c and int(a[i]) > 0:
            res += 1
    return res

print(solve(n, k))
