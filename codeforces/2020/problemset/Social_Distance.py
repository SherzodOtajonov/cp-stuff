t = int(input())

def solve(n, k, s):
    if set(s) == set('0') and n==k: return 1
    res = curr = 0
    for i in range(n):
        if s[i] == '0' and i == n-1:
            curr += 1
        if s[i] != '0' or i == n-1:
            res += curr//(k+1)
            curr = 0
        else: curr += 1
    return res

for i in range(t):
    n, k = [int(j) for j in input().split()]
    s = input()
    print(solve(n, k, s))
