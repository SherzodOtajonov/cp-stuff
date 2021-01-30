t = int(input())
 
from math import ceil
def solve(n, a):
    odds = evens = 0
    for i in range(n):
        if a[i]%2==0: evens +=1
        else: odds +=1
    if not odds: return -1
    else: return evens
 
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
