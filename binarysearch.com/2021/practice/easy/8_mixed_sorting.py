class Solution:
    def solve(self, nums):
        odd, even = [], []
        for i in range(len(nums)):
            if nums[i]%2: 
                odd.append(nums[i])
                nums[i] = 1
            else:
                even.append(nums[i])
                nums[i] = 0 
        odd.sort()
        even.sort(reverse=True)
        print(odd, even, nums)
        for i in range(len(nums)):
            if nums[i]: nums[i] = odd.pop()
            else: nums[i] = even.pop()
        return nums
        
