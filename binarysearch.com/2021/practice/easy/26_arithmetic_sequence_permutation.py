class Solution:
    def solve(self, nums):
        nums.sort()
        c = abs(nums[0]-nums[1])
        for i in range(2, len(nums)):
            if c != abs(nums[i-1] - nums[i]):
                return False
        return True
