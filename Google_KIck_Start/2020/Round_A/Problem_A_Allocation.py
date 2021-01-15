T = int(input())

def solve(n, b, a):
    a.sort()
    c = res = 0
    for i in a:
        if res+i <= b:
            c += 1
            res += i
        else:
            break    
    return c
    
for i in range(1, T+1):
    N, B = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    print('Case #{}: {}'.format(i, solve(N, B, A)))
