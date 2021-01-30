class Solution:
    def solve(self, nums):
        neg, pos = [], []
        for i in nums:
            if i == 0:
                neg.append(0)
                pos.append(0)
            elif i<0: neg.append(i)
            else: pos.append(i)
        neg.sort()
        for i in neg:
            if i*(-1) in pos: return i*(-1)
        return -1
