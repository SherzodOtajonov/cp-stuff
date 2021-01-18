from collections import Counter
class Solution:
    def solve(self, nums):
        for k, v in Counter(nums).items():
            if k == v: return True
        return False
