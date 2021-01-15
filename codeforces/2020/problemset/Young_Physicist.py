n = int(input())

def solve(n):
    x = y = z  = 0
    for i in range(n):
        a, b, c = [int(j) for j in input().split(' ')]
        x+=a
        y+=b
        z+=c
    if x==0 and y==0 and z==0: return 'YES'
    return 'NO'
print(solve(n))
