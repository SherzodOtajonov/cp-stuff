class Solution:
    def solve(self, nums):
        if not nums: return 0
        l = []
        for i in nums:
            if i>=0 and l and l[-1] != 1: l.append(1)
            elif i<0 and l and l[-1] != 0: l.append(0)
            elif i>=0 and not l: l.append(1)
            elif i<0 and not l: l.append(0)
        
        return len(l)
