t = int(input())


def solve(a, b):
    if a>b:
        if a%2:
            return a*a-(a*2-1-b)
        else:
            return a*a-b+1
    else:
        if b%2==0:
            return b*b-(b*2-1-a)
        else:
            return b*b-a+1
        

for i in range(t):
    a, b = map(int, input().split(' '))
    print(solve(a, b))
