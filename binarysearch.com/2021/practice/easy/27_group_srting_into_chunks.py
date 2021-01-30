class Solution:
    def solve(self, s, n):
        if len(s)<=n: return [s]
        r=[]
        i=0
        while i+n<=len(s):
            r.append(s[i:i+n])
            i+=n
        if len(s)%n != 0:
            r.append(s[i:])
        return r
