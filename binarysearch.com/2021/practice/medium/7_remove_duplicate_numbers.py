from collections import Counter
class Solution:
    def solve(self, nums):
        c = Counter(nums)
        l = []
        for i in nums:
            if c[i] == 1:
                l.append(i)
        return l
