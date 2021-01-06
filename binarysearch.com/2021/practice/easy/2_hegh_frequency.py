from collections import Counter
class Solution:
    def solve(self, nums):
        return Counter(nums).most_common(1)[0][1]
