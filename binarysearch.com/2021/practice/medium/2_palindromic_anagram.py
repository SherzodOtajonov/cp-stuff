from collections import Counter
class Solution:
    def solve(self, s):
        c = 0
        for i in Counter(s).values():
            if i%2: c+=1
            if c>1: return False
        return True
