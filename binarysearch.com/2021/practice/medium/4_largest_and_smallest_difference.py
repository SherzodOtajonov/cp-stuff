class Solution:
    def solve(self, nums, k):
        k-=1
        nums.sort()
        df = nums[-1]-nums[0]
        for i in range(len(nums)-k):
            df = min(df, nums[i+k]-nums[i])
        return df
