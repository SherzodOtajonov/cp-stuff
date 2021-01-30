from collections import Counter
class Solution:
    def solve(self, s):
        c = Counter(s)
        if c['z'] == 1: return 0
        return min(c['p'], c['i'], c['z']//2, c['a'])
