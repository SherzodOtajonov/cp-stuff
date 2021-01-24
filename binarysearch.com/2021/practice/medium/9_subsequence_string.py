class Solution:
    def solve(self, s1, s2):
        if not s1: return True
        c=0
        for i in s2:
            if i == s1[c]:
                c+=1
            if c >= len(s1): return True
        return False
            
