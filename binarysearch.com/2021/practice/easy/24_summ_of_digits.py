class Solution:
    def solve(self, num):
        r=0
        while num:
            r+= num%10
            num= num//10
        return r
