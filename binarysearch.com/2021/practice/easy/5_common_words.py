class Solution:
    def solve(self, s0, s1):
        if not s0 or not s1: return 0
        a = [i.lower() for i in s0.split(' ')]
        b = [i.lower() for i in s1.split(' ')]
        return len(set(a) & set(b))
