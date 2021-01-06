from collections import Counter
class Solution:
    def solve(self, nums):
        c = Counter(nums)
        return len(set(c.values())) == len(c.values())
