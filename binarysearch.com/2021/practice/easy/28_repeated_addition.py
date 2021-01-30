class Solution:
    def solve(self, n):
        r=0
        while True:
            while n:
                r+=n%10
                n=n//10
            if r>=10: 
                n=r
                r=0
            else: break
        return r
