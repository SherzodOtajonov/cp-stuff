class Solution:
    def solve(self, prices, k):
        if not prices: return 0
        r=0
        for i in sorted(prices):
            if k>=i:
                k-=i
                r+=1
            else:
                return r
        return r
