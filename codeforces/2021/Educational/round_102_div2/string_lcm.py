from math import gcd
 
t = int(input())
 
def solve(s, t):
    lcm = (len(s)*len(t))/gcd(len(s), len(t))
    s *= int(lcm/len(s))
    t *= int(lcm/len(t))
    if s == t:
        return s
    return -1
 
 
for i in range(t):
    s = input().strip()
    t = input().strip()
    print(solve(s, t))
