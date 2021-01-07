class Solution:
    def solve(self, nums):
        from itertools import product
        odds = evens = 0
        for i in nums:
            if i%2: odds +=1
            else: evens +=1
        return evens*odds     
