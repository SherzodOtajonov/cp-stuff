x, y, z = [int(i) for i in input().split()]

def solve(x, y, z):
    if x>z+y:
        return '+'
    if y>x+z:
        return '-'
    if z==0 and x==y:
        return '0'
    return '?'

print(solve(x, y, z))
