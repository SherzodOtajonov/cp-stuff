n = int(input())
s = input()

def solve(s, n):
    from collections import defaultdict
    d = defaultdict(lambda : 0)
    for i in range(n-1):
        d[s[i:i+2]] += 1

    return max(d, key=d.get)

print(solve(s, n))
