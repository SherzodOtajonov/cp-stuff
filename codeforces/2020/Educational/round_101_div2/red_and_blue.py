t = int(input())
 
def solve(r, b):
    blue = red = bt = rt = 0
    for i in range(max(len(r), len(b))):
        if i < len(r):
            rt += r[i]
            red = max(red, rt)
        if i < len(b):
            bt += b[i]
            blue = max(blue, bt)
    return red + blue
 
    
for i in range(t):
    input()
    r = list(map(int, input().split(' ')))
    input()
    b = list(map(int, input().split(' ')))
    print(solve(r, b))

# same issue here, i couldnt understand the problem again...
