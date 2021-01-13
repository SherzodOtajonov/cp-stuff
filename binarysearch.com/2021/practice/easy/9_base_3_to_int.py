class Solution:
    def solve(self, s):
        r = i = 0
        for j in range(len(s)-1, -1, -1):
            r+= int(s[j])*3**i
            i+=1
        return r
