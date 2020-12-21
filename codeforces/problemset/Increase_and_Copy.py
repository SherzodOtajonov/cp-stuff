t = int(input())

def solve(n):
    for i in range(n-1, 0, -1):
        if n%i == 0:
            return (i-1) * (n/i-1)


for j in range(t):
    n = int(input())
    print(solve(n))

