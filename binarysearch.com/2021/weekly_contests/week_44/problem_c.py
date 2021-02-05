class Solution:
    def solve(self, nums):
        if len(nums)==0: return 0
        r=0
        for i in range(len(nums)):
            mn, mx = nums[i], nums[i]
            for j in range(i+1, len(nums)):
                c = nums[i:j+1]
                if nums[j]>mx: mx=nums[j]
                if nums[j]<mn: mn=nums[j]
                if mx-mn+1 == len(c): r = max(r, mx-mn+1)
        return max(r, 1)
