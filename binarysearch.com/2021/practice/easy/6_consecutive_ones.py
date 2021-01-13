class Solution:
    def solve(self, nums):
        if len(nums) <= 2: return 1 in nums

        flag = False
        c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c+=1
                flag = True
            if flag and nums[i] != 1:
                return nums.count(1) == c 
        return True
