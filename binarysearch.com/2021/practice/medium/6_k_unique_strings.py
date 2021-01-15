from collections import Counter
class Solution:
    def solve(self, s, k):
        c = Counter(s)
        if len(c)==k: return 0
        else:
            l = sorted(c.values(), reverse=True)
            return sum(l[k:len(l)])
