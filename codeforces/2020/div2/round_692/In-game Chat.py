t = int(input())


def solve(n, s):
    c = 0
    for i in range(n-1, -1, -1):
        if c > n-c:
            return True
        if s[i] == ')':
            c += 1
        else:
            break
    return c > n-c

for i in range(t):
    n = int(input())
    s = input()
    if solve(n, s):
        print('Yes')
    else:
        print('No')
