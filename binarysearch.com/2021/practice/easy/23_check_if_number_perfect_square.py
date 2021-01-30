class Solution:
    def solve(self, n):
        if not n: return True
        i=0
        while True:
            i+=1
            if i*i==n: return True
            if i*i>n: return False
